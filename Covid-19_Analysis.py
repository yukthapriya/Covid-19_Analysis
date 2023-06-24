#!/usr/bin/env python
# coding: utf-8




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

# Plotting the timeline of the number of cases per day (not cumulative) for a specific country
country_name = "United States"
dates = [date for date in timeline.keys()]
cases = [next((country["Confirmed"] for country in countries if country["Country"] == country_name), 0) for countries in timeline.values()]

plt.plot(dates, cases)
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.title(f"Timeline of COVID-19 cases in {country_name}")
plt.xticks(rotation=45)
plt.show()


