import sys
from datetime import datetime 

current_date=None
current_news=""
for line in sys.stdin:
    line=line.strip()
    line=line.split('|')
    if(len(line)<2):
        continue
    date=line[0]
    news=line[1]
    try:
        # Attempt to convert the date string to a datetime object
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        # If conversion fails, it's not in the expected format
        pass
    if(current_date==date):
        current_date=date
        current_news+='.'+news
    else:
        if(current_date !=None ):
            print('%s|%sa'%(current_date,current_news))
        current_date=date
        current_news=news
if(current_date):
    print('%s|%sa'%(current_date,current_news))
    
	
    
