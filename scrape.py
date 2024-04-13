import requests
from bs4 import BeautifulSoup
import csv

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"
def scrape() :
    headers=["Name", "Distance", "Mass", "Radius"]
stars_data = []

response = requests.get(START_URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')  
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 3:  
        name = cols[0].text.strip()
        distance = cols[1].text.strip()
        mass = cols[2].text.strip()
        radius = cols[3].text.strip()
        stars_data.append([name, distance, mass, radius])

with open('stars_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Distance', 'Mass', 'Radius'])
    writer.writerows(stars_data)