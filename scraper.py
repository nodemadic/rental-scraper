import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.zillow.com/homes/for_sale/San-Francisco_rb/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

listings = []

for listing in soup.find_all('div', {'class': 'property-card-data'}):
    result = {}
    result['address'] = listing.find('address', {'data-test': 'property-card-addr'}).get_text().strip()
    result['price'] = listing.find('span', {'data-test': 'property-card-price'}).get_text().strip()
    details_list = listing.find('ul', {'class': 'dmDolk'})
    details = details_list.find_all('li') if details_list else []
    result['bedrooms'] = details[0].get_text().strip() if len(details) > 0 else ''
    result['bathrooms'] = details[1].get_text().strip() if len(details) > 1 else ''
    result['sqft'] = details[2].get_text().strip() if len(details) > 2 else ''
    type_div = listing.find('div', {'class': 'gxlfal'})
    result['type'] =  type_div.get_text().split("-")[1].strip() if type_div else ''

    listings.append(result)

with open('/app/output-logs/output.txt', 'w') as file:
    file.write(json.dumps(listings, indent=4))
