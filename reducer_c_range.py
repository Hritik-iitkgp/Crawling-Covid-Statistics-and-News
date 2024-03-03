import sys
from datetime import datetime


current_country=None
current_time=""

for line in sys.stdin:
    line=line.strip()
    line=line.split('|')
    if(len(line)<2):
        continue
    country=line[0]
    time=line[1]
    try:
        # Attempt to convert the date string to a datetime object
        datetime.strptime(time, "%Y-%m-%d")
    except ValueError:
        # If conversion fails, it's not in the expected format
        pass
    if(current_country==country):
        current_country=country
        current_time+=' '+time
    else:
        if(current_country != None):
            print('%s\t%s'%(current_country,current_time))
        current_country=country
        current_time=time
if(current_country !=None):
    time_range=current_time.split(" ")
    start=time_range[0]
    end=time_range[-1]
    print('%s\t%s\t%s'%(current_country,start,end))