import sys

f=sys.argv[1]
file1=open(f,'r')
country=sys.argv[2]
print('%s\t'%(country))
query=int(sys.argv[3])
for line in file1:
    line=line.strip()
    data=line.split('|')
    node1=data[0]
    if(query==1):
        node2=data[1] #Total cases
    elif(query==2):
        node2=data[2] #Active cases
    elif(query==3):
        node2=data[3] #Total deaths
    elif(query==4):
        node2=data[4] # Total recovered
    elif(query==5):
        node2=data[5] #Total tests
    elif(query==6):
        node2=data[6] #Death/million
    elif(query==7):
        node2=data[7] #Tests/million
    elif(query==8):
        node2=data[8] #New case
    elif(query==9):
        node2=data[9] #New death
    elif(query==10):
        node2=data[10] #New recovered
    if(node1 not in ['Asia','North America','Europe','South America','Oceania','Africa']):
        print('%s|%s'%(node1,node2))
file1.close()
