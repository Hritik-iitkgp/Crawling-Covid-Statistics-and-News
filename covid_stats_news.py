import os
import subprocess
from datetime import datetime

def get_country_statistic(country):
    # Simulated function to fetch statistics for the given country from the database or API
    statistics = {
        "total_cases": 1000,
        "active_cases": 500,
        "total_deaths": 100,
        "total_recovered": 400,
        "total_tests": 5000,
        "death_per_million": 50,
        "tests_per_million": 500,
        "new_cases": 50,
        "new_deaths": 10,
        "new_recovered": 30
    }
    return statistics

def show_country_statistics():
    country = input("Enter the country name: ")
    print(f"Displaying statistics for {country}...")
    
    while True:
        print("\nSelect the type of statistic:")
        print("a. Total cases")
        print("b. Active cases")
        print("c. Total deaths")
        print("d. Total recovered")
        print("e. Total tests")
        print("f. Death/million")
        print("g. Tests/million")
        print("h. New case")
        print("i. New death")
        print("j. New recovered")
        print("k. Back to country selection")
        
        choice = input("Enter your choice (a-k): ")
        statistic_mapping = {
            'a': 'total_cases',
            'b': 'active_cases',
            'c': 'total_deaths',
            'd': 'total_recovered',
            'e': 'total_tests',
            'f': 'death_per_million',
            'g': 'tests_per_million',
            'h': 'new_cases',
            'i': 'new_deaths',
            'j': 'new_recovered'
        }
        
        if choice == 'k':
            print("Returning to the country selection...")
            break
        elif choice in statistic_mapping:
            statistic_type = statistic_mapping[choice]
            country_statistic = get_country_statistic(country)
            if statistic_type in country_statistic:
                print(f"{statistic_type.replace('_', ' ').title()}: {country_statistic[statistic_type]}")
            else:
                print("Invalid statistic type. Please enter a valid option.")
        else:
            print("Invalid choice. Please enter a valid option.")

# Include the main() function and the menu code from the previous example here
def show_country_statistics():
    country = input("Enter the country name: ")
    print(f"Displaying statistics for {country}...")
    # Add your logic to display statistics specific to the entered country

def show_statistics():
    while True:
        print("\nStatistics Menu:")
        print("1. All Statistics")
        print("2. Country-wise Statistics")
        print("3. Back to main menu")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            show_all_statistics()
        elif choice == '2':
            show_country_statistics()
        elif choice == '3':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Include the main() function and the menu code from the previous example here


def show_response_news(what):
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    try:
        date_str = input(prompt)
        date = datetime.strptime(date_str, "%Y-%m-%d")  
    except ValueError:
        print("Invalid date format.")
        show_response_news(what)
    print(f"Displaying news from {start_date} to {end_date}...")
    if(what=='response' or what=='news'):
        file1 = os.listdir(what)
        file1=[os.path.join(what, i) for i in file1]
    else:
        file1=os.listdir('countries')
        file1=[os.path.join('countries', i) for i in file1 if (what in i)]
    file1=' '.join(file1)
    # Add your logic to display response news based on the date range
    command = "python3 mapper.py "+ file1 +" "+ start_date+ " "+end_date+"| sort -n | python3 combiner.py ;wait | sort -n| python3 reducer.py"
    print(command)
    return
    # Execute shell command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Shell command executed successfully!")
    else:
        print("Error executing shell command:")
        print(result.stderr)	
        
def show_country_news():
    country = input("Enter the country name: ")
    print(f"Range for which news is present {country}...")
    directory_path = "countries"
    files = os.listdir(directory)
    dates=[]
    flag=1
    paths=[]
    for i in files:
        if(country in i):
            years=['2019','2020','2021','2022','2023','2024']
            year = [value for value in years if value in i][0]
            flag=0
            file_path = os.path.join(directory_path, i)
            year=i.split('_')[1].split('.')[0]
            paths.append(i)
            f=open(file_path)
            for line in f:
                date, _ = line.strip().split(':')
                if(date.split()[0].isdigit()):
                    dates.append(year+"-"+date.split()[1])
                else:
                    dates.append(year+"-"+date.split()[0]+year)
    if(flag):
        print("Please Enter valid country name")
        show_country_news()
    start,end=min(dates),max(dates)
    show_response_news(country)
    
def show_news():
    while True:
        print("\nNews Menu:")
        print("1. Response News")
        print("2. Timeline News")
        print("3. Country News")
        print("4. Back to main menu")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            show_response_news('response')
        elif choice == '2':
            show_response_news('news')
        elif choice == '3':
            show_country_news()
        elif choice == '4':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Include the main() function and the menu code from the previous example here

def main():
    while True:
        print("\nMenu:")
        print("1. Statistics")
        print("2. News")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            show_statistics()
        elif choice == '2':
            show_news()
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

