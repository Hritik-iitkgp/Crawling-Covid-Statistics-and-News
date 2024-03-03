import sys
import re
from datetime import datetime

f=sys.argv[1]
file1=open(f,'r')
start_date=sys.argv[-2]
end_date=sys.argv[-1]
def extract_year_from_filename(filename):
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
for line in file1:
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
        print('%s|%s'%(formated_date,text))
    else:
        print("Error",formated_date)
file1.close()
