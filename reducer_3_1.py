import sys

current_count=0
current_country=None
total_count=0

for line in sys.stdin:
    line=line.strip()
    line=line.split('|')
    if(len(line)==1):
     current_country=line[0]
     continue
    else:
        node1=line[0]
        node2=line[1]
        count=line[2]
    try:
        count=float(count.replace(',','')) if(count!="N/A") else 0
        node2=float(node2.replace(',','')) if(node2!="N/A") else 0
    except ValueError:
        continue
    if(current_country==node1):
        current_count=node2
        total_count+=count
    else:
        total_count+=count
percentage=float(float(current_count/total_count)*100)
print("{}\t{} ".format(current_country,int(current_count)))
print("{}\t{:.2f} %".format(current_country,percentage))

