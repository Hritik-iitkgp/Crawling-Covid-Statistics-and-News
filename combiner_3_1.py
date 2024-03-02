import sys

current_count=0
current_country=None
total_count=0
for line in sys.stdin:
    line=line.strip()
    line=line.split('|')
    if(len(line)==1):
     current_country=line[0]
     print("%s"%(current_country))
     continue
    else:
        node1=line[0]
        node2=line[1]
    try:
        node2=float(node2.replace(',','')) if(node2!="N/A" or node2!='-') else 0
    except ValueError:
        pass
    if(current_country.lower() in node1.lower()):
        current_count=node2
        #print(node2)
        total_count+=current_count
    else:
        total_count+=node2
print("%s|%d|%d"%(current_country,current_count,total_count))

