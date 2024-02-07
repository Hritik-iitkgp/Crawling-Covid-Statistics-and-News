import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
from urllib.error import HTTPError


req = Request('https://www.worldometers.info/coronavirus/')
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('worldometer.html','w',encoding="utf-8")
f.write(mydata)
f.close

f1=open('worldometers_countrylist.txt', 'r')
for line in f1:
	line=line.strip()
	line='-'.join([i.lower() for i in line.split()])
	if (line!='europe:' and line!='north-america:' and line!='asia' and line!='south-america' and line!='africa' and line!='oceania'and line!='' ):
		if(line[-1]!='-'):
			req1 = Request('https://www.worldometers.info/coronavirus/country/'+line +'/')
			try:
				webpage1 = urlopen(req1).read()
				data = webpage1.decode("utf8")
				with open(f'{line}.html', 'w', encoding="utf-8") as f2:
					f2.write(data)
					f2.close
			except HTTPError as e:
				print(f"HTTP Error  {e.code}: {e.reason} for URL: {req1.full_url} ")
f1.close
