import sys
import re
from datetime import datetime

f=sys.argv[1]
country=sys.argv[-2]
def find_country_name(text):
    pattern = r'([A-Za-z]+)'
    text=text.split('/')
    text=text[-1]
    match = re.match(pattern, text.split('_')[0])
    if match:
        # Extract the country name and year from the matched groups
        country_name = match.group(1)
        #print(country_name)
        
    else:
        country_name=None
    return country_name

time_range=sys.argv[-1]
time_range=time_range.replace('[','')
time_range=time_range.replace(']','')
time_range=time_range.split(',')
#print(time_range)
start_date=time_range[0]
end_date=time_range[1]


def extract_year_from_filename(filename):
    filename=filename.split('/')
    filename=filename[-1]
    # Try to extract the first four characters as the year
    year_str  = re.search(r'\d{4}\b|\b\d{4}', filename)
    try:
        # Convert the extracted string to an integer
        year = int(year_str.group())
        return year
    except ValueError:
        # Handle the case when conversion to integer fails
        return None

def convert_to_date(date_str, year):
    # Split the input date string into components
    date_components = date_str.split()

    # Check the order of day and month
    if date_components[0].isdigit():
        # If day is the first component, use the format "%d %B %Y"
        date_format = "%d %B %Y"
    else:
        # If month is the first component, use the format "%B %d %Y"
        date_format = "%B %d %Y"

    # Concatenate the year with the date string
    date_with_year = "{} {}".format(date_str, year)
    # Parse the string to a datetime object
    try:
        datetime_object = datetime.strptime(date_with_year, date_format)
        # Extract only the date component
        date_only = datetime_object.date()
        return date_only
    except ValueError:
        return None
    
year=extract_year_from_filename(f)  
country_name=find_country_name(f)

if(country_name!=None and country_name.lower()==country.lower()):
    file1=open(f,'r')
    for line in file1:
        #print("filre ")
        line=line.strip()
        data=line.split(':')
        date=data[0]
        text=data[1]
        if(date==None):
            continue
        formated_date=convert_to_date(date,year)
        start_date_o=datetime.strptime(start_date,"%d-%m-%Y")
        s_start_date=start_date_o.date()
        end_date_o=datetime.strptime(end_date,"%d-%m-%Y")
        e_end_date=end_date_o.date()
        if(formated_date!=None and formated_date>=s_start_date and formated_date<=e_end_date):
            print('%s|%s'%(country_name,formated_date))
    file1.close()

    
