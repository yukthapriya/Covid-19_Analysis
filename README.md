# Covid-19_Analysis
Based on a dataset that contains the cumulative number of covid cases for a state/country.
A small program that would download the dataset, and displays the following information:
1.  Countries having more than 5000000 confirmed cases by 29th May 2021.
2.  Name of the state/country having the most number of recovery on a day.
3.  Timeline of the number of cases per day (not cumulative) by state/country.
4.  Timeline of the status of the countries. Countries with more than 500,000 cases on that day, should be classified as red, more than 100,000 as orange, more than 
     10,000 as yellow, and others as green.
    
    
Dataset:
The dataset can be found in JSON format here:

https://raw.githubusercontent.com/niranjanthiru/covid_cases_vaccination/855fd25e68f50b009f7ed88252fa3e4e70b54dfb/covid_19_data.json
The JSON dataset has the data from 1st Jan 2021 to 29th May 2021
 
And is documented here: https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset?select=covid_19_data.csv
 
# Tools Required

python 3.8
Jupyter Notebook
Anaconda
# Implementation
# import the packages

import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt

# Download the dataset

url = "https://raw.githubusercontent.com/niranjanthiru/covid_cases_vaccination/855fd25e68f50b009f7ed88252fa3e4e70b54dfb/covid_19_data.json"
response = requests.get(url)
data = response.json()

# Filter countries with more than 5,000,000 confirmed cases by 29th May 2021

high_cases_countries = [country for country in data if country["Confirmed"] > 5000000 and country["ObservationDate"] == "05/29/2021"]

# the state/country with the most number of recoveries on a day

most_recoveries_country = max(data, key=lambda x: x["Recovered"])

# Extract the timeline of the number of cases per day by state/country

timeline = {}
for country in data:
    date = datetime.strptime(country["ObservationDate"], "%m/%d/%Y")
    if date in timeline:
        timeline[date].append(country)
    else:
        timeline[date] = [country]

# status timeline
status_timeline = {}
for date, countries in timeline.items():
    status_timeline[date] = {}
    for country in countries:
        if country["Confirmed"] > 500000:
            status = "red"
        elif country["Confirmed"] > 100000:
            status = "orange"
        elif country["Confirmed"] > 10000:
            status = "yellow"
        else:
            status = "green"
        status_timeline[date][country["Country"]] = status

# Display the information
print("Countries with more than 5,000,000 confirmed cases by 29th May 2021:")
for country in high_cases_countries:
    print(country["Country"])

print("\nState/Country with the most number of recoveries on a day:")
print(most_recoveries_country["Country"])


print("\nTimeline of the number of cases per day (not cumulative) by country:")
for date, countries in timeline.items():
    print(f"{date.strftime('%m/%d/%Y')}:")
    for country in countries:
        print(f"{country['Country']}: {country['Confirmed']} cases")



print("\nTimeline of the status of the countries:")
for date, countries in status_timeline.items():
    print(f"{date.strftime('%m/%d/%Y')}:")
    for country, status in countries.items():
        print(f"{country}: {status}")





