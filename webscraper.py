import requests
import csv
from bs4 import BeautifulSoup

base_url = "http://ergast.com/api/f1/"

# Start scraping from 2000 to 2022 for past 2 decades
for yearInt in range(2000, 2023):
    
    year = str(yearInt)

    # Define the URL to fetch the results for the specified year
    url = f"{base_url}{year}/results/"

    # Send a GET request to the Ergast API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
    
        # Parse the XML response
        soup = BeautifulSoup(response.content, 'xml')
        total_value = soup.find('MRData')['total']
        

        url = f"{base_url}{year}/results/?limit={total_value}&offset=0"   
        response = requests.get(url) 
        soup = BeautifulSoup(response.content, 'xml')  

        # Find all Race tags
        races = soup.find_all('Race')
        
        # List to store race data
        race_data = []

        # Iterate over each Race
        for race in races:
            
            # Find all Result tags within each Race
            results = race.find_all('Result')
            
            # Count the number of 'R' in the position attribute
            r_count = sum(1 for result in results if result['positionText'] == 'R')
            
            # Get the race name & remove the Grand Prix part for plotting
            race_name = race.find('RaceName').text.replace(" Grand Prix", "")
            
            # Append race data to the list
            race_data.append({'Race': race_name, 'DNF': r_count})
            
            
        # Write race data to a CSV file
        with open(f'race_results_{year}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Race', 'DNF']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for data in race_data:
                writer.writerow(data)
            
    else:
        # Print an error message if the request was unsuccessful
        print("Error fetching data from the Ergast API.")
