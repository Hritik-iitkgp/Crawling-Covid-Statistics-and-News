Github link : ```https://github.com/Hritik-iitkgp/Crawling-Covid-Statistics-and-News/tree/main```

# Crawling-Covid-Statistics-and-News


## Overview

This project involves creating a user-friendly system for extracting and managing COVID-19-related data from Worldometer ( https://www.worldometers.info/coronavirus/ )  and Wikipedia ( https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic ) using Lex, Yacc, and NoSQL paradigms. The system is divided into modules, each focusing on specific tasks, and the extracted information is stored in text files. The system allows users to query and retrieve relevant data based on specific criteria. Follow the below for getting more information about it :)

### Run the code by following coomand
```python3 covid_stats_news.py```


## Modules

### Module 1: Crawling Worldometer Website

- Crawl over Worldometer ( https://www.worldometers.info/coronavirus/ ) website for getting COVID-19 statistics.
- Extract and save data for countries listed in "worldometers_countrylist.txt", stored in Worldometers_countrylist_html folder.
- Create grammar for extracting specific fields (Total cases, Active cases, Total deaths, Total recovered, Total tests, Death/million, Tests/million, New case, New death, New recovered) from the data. 


### Module 2: Crawling Wikipedia COVID-19 Timeline

- Crawl Wikipedia COVID-19 timeline page ( https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic ).
- Extract worldwide news and responses and also the time line countries data.
- Store results in text files based on time ranges and countries.
- Stored in countries, news and response folders.
- All the scrapers present in scraper.py

### Module 3.1: Addressing Queries of Worldometer COVID Statistics

- Use MapCombineReduce paradigm to address queries.
- Retrieve and display COVID statistics for each country.
- Calculate percentage of total world cases.
- used mapper3.1.py, combiner3.1.py, reducer3.1.py


### Module 3.2: Addressing Queries of Wikipedia COVID News

- Utilized the MapCombineReduce paradigm for data retrieval.
- Address user queries related to worldwide news and responses.
- used mapper.py, combiner.py, reducer.py


### Module 4: Combining Modules 3.1 and 3.2

- Combine NoSQL queries for both Worldometer and Wikipedia data.
- User-friendly menu system for accessing modules for easy use.


# Project Contributors

Special thanks to the contributors who worked on this project:

- [@Aarati_Shah](https://github.com/Antlia360)
- [@Hritik_Jaiswal](https://github.com/Hritik-iitkgp)
- [@Rupali_Kalundia](https://github.com/Ru-pali10)


https://drive.google.com/file/d/1lHzGYQIgE0f9pdv3w9il1C007mb8FEGf/view?usp=sharing

### Feel free to contribute :smile:
