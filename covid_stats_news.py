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

def show_all_statistics():
    country = input("Enter the country name: ")
    print(f"Displaying statistics for {country}...")
    
    while True:
        print("\nSelect the type of statistic:")
        print("1. Total cases")
        print("2. Active cases")
        print("3. Total deaths")
        print("4. Total recovered")
        print("5. Total tests")
        print("6. Death/million")
        print("7. Tests/million")
        print("8. New case")
        print("9. New death")
        print("10. New recovered")
        print("11. Back to country selection")
        
        choice = input("Enter your choice (1-11): ")
        if choice == '11':
            print("Returning to the country selection...")
            break
        elif int(choice) in range(1,12):
            command = " python3 mapper_3.1.py table.txt "+ country+" " +choice+" | sort -n| python3 reducer.py"
            print(command)
            # Execute shell command
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
            # Check if the command was successful
            if result.returncode == 0:
                print("Shell command executed successfully!")
                print(result.stdout)
            else:
                print("Error executing shell command:")
                print(result.stderr)
        else:
            print("Invalid choice. Please enter a valid option.")


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
            print('current data not fetched from website')
        elif choice == '3':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")



def show_response_news(what):
    start_date = input("Enter the start date (DD-MM-YYYY): ")
    end_date = input("Enter the end date (DD-MM-YYYY): ")
    try:
        date = datetime.strptime(start_date, "%d-%m-%Y")  
        date1 = datetime.strptime(end_date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format.")
        show_response_news(what)
        return
    print(f"Displaying news from {start_date} to {end_date}...")
    if(what=='response' or what=='news'):
        file1 = os.listdir(what)
        file1=[os.path.join(what, i) for i in file1]
    else:
        file1=os.listdir('countries')
        file1=[os.path.join('countries', i) for i in file1 if (what.lower() in i.lower())]
    command='('
    for i in file1:
        command+="python3 mapper.py "+i+" "+ start_date+ " "+end_date+" | sort -n | python3 combiner.py ;wait &"
    command+=')'
    # Add your logic to display response news based on the date range
    # $(MAPPER)  $(INPUT_FILE) | sort -n | $(COMBINE);wait &
    command += "  | sort -n| python3 reducer.py"
    print(command)
    # Execute shell command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        print("Shell command executed successfully!")
        print(result.stdout)
    else:
        print("Error executing shell command:")
        print(result.stderr)	
        
def show_country_news():
    country = input("Enter the country name: ")
    print(f"Range for which news is present {country}: ")
    directory_path = "countries"
    files = os.listdir(directory_path)
    dates=[]
    flag=1
    paths=[]
    for i in files:
        if(country.lower() in i.lower()):
            years=['2019','2020','2021','2022','2023','2024']
            year = [value for value in years if value in i.lower()][0]
            flag=0
            file_path = os.path.join(directory_path, i)
            paths.append(i)
            f=open(file_path)
            for line in f:
                date, _ = line.strip().split(':')
                if 'On' in date:
                    date=date[3:]
                if(len(date.split())<2):
                    continue
                if(date.split()[0].isdigit()):
                    dates.append(year+"-"+date.split()[1])
                else:
                    dates.append(year+"-"+date.split()[0]+year)
    if(flag):
        print("Please Enter valid country name")
        show_country_news()
        return
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

