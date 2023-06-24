# Covid-19_Analysis (Final Assignment)
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
# Importing necessary libraries and modules:

The requests library is used for making HTTP requests to download the dataset, json library is used for parsing the JSON data, and datetime module is used for handling dates.

# Downloading the dataset
The code downloads the dataset from the provided URL and stores the JSON response in the data variable.

Extracting the timeline of the number of cases per day by state/country:

                              timeline = {}
                              for country in data:
                                  date = datetime.strptime(country["ObservationDate"], "%m/%d/%Y")
                                  if date in timeline:
                                      timeline[date].append(country)
                                  else:
                                      timeline[date] = [country]

This loop iterates over each entry in the dataset and extracts the observation date and country information. It creates a dictionary called timeline where the keys are the dates, and the values are lists of countries with their respective case information on that date.

Displaying the timeline of the number of cases per day (not cumulative) by state/country:

                              for date, countries in timeline.items():
                                  print(f"{date.strftime('%m/%d/%Y')}:")
                                  for country in countries:
                                      print(f"{country['Country/Region']}: {country['Confirmed']} cases")
                                  print()



This loop iterates over the items in the timeline dictionary. For each date, it prints the date in the format "MM/DD/YYYY". Then, it iterates over the list of countries on that date and prints the country name along with the number of confirmed cases. After printing the cases for a specific date, it prints an empty line to separate the information for different dates.

By executing this code, you will see the timeline of the number of cases per day (not cumulative) by state/country, with each date followed by a list of countries and their respective confirmed cases on that date.
