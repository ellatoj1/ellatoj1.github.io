import requests
from bs4 import BeautifulSoup  
import json  
import os  

# the URL of the webpage that we want to scrape
url = "https://realpython.github.io/fake-jobs/" 

# sending a GET request to the specified URL
response = requests.get(url) 
response.raise_for_status()  # raises an HTTPError if the HTTP request returned an unsuccessful status code

# parsing the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# extracting all the job cards (each job listing) from the HTML by finding all div elements with the class 'card-content'
job_cards = soup.find_all('div', class_='card-content')

# creating an empty list to store job data
jobs = []

# iterating over each job card extracted from the HTML
# the structure of each job card is determined by inspecting the HTML of the webpage
for card in job_cards:
    title = card.find('h2', class_='title').text.strip()  
    company = card.find('h3', class_='company').text.strip() 
    location = card.find('p', class_='location').text.strip().title()  
    date_posted = card.find('time').text.strip() 

    jobs.append({
        'Job Title': title,
        'Company': company,
        'Location': location,
        'Date Posted': date_posted
    })

# output file path for the JSON file
output_path = os.path.join(os.getcwd(), 'job_search_v2.json') 

with open(output_path, 'w') as f: 
    json.dump(jobs, f, indent=4)  # writing the JSON data to the file with an indentation of 4 spaces for readability

# printing a confirmation message indicating that the JSON file has been created when the script is run
print(f'Job data has been written to {output_path}')
