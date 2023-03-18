# Importing required modules
import requests
from bs4 import BeautifulSoup


# Taking url and setuping the soup 
url  = '''https://thehackernews.com'''
data =  requests.get(url,'html.parser').content
soup  = BeautifulSoup(data,features='html.parser')


# Creating the list to store the data
dates  = []
titles  = []
years = []
crime_type = []
attack = []


# Scraping using the class
web_dates = soup.find_all(class_='item-label')
web_names = soup.find_all(class_='home-title')


# Popping the unnecessary element
web_dates.pop(2)
web_names.pop(2)


# Storing in the variables accordingly
for e,i in enumerate(web_dates):
    dates.append(i.text.split(',')[0][2:])
    years.append(i.text.split(',')[1][1:5])
    crime_type.append(i.text.split(',')[1].split('/')[0][6:])
    attack.append(i.text.split(',')[1].split('/')[1].replace('\n','')[1:])


# Storing the titles
for i in web_names: 
    titles.append(i.text)


# Creating the Dataframe to convert into csv file
import pandas as pd
scraped_data = {
                'Date':dates,
                'Year':years,
                'Title':titles,
                'Crime type':crime_type,
                'Attack type':attack
                }
df = pd.DataFrame(scraped_data)
print('The DataFrame is :')
print(df.head())
print('\n')
df.to_csv('web_data.csv')

# Converting into the json string
import json
json_container  = json.dumps(scraped_data)
print('The json data :')
print(json_container)


# Creating a json file to store the json data
with open('web_Data.json','w') as file:
    file.write(json_container)