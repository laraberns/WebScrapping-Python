import requests
from bs4 import BeautifulSoup

def extractData(url, category):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all("div", class_="card shadow")
        
        for card in cards:
            # Extract Event Name
            event_name = card.find("p", class_="card-text")
            event_name = event_name.text.strip() if event_name else "No name found"
            
            # Extract Event Date
            event_date = card.find("div", class_="card-title")
            event_date = event_date.text.strip() if event_date else "No date found"
            
            # Extract Event Place 
            event_place = card.find("span", class_="text-muted")
            event_place = event_place.text.strip() if event_place else "No place found"

            # Extract Event Link 
            event_link = card.find("a", class_="text-dark font-weight-bold text-decoration-none stretched-link")
            event_link = event_link['href'] if event_link else "No link found"

            # Extract Event Photo
            event_photo = card.find("img", class_="card-img-top border-bottom")
            event_photo = event_photo['src'] if event_photo else "No photo found"
            
            # Print the extracted data along with category
            print(f"Category: {category}")
            print(f"Event Name: {event_name}")
            print(f"Event Date: {event_date}")
            print(f"Event Place: {event_place}")
            print(f"Event Link: {event_link}")
            print(f"Event Photo: {event_photo}")
            print("-" * 40)
    else:
        print(f"Error: {response.status_code} for category {category}")

categories = [
    {"url": "https://www.pensanoevento.com.br/eventos/", "cl": "Eventos"},
    {"url": "https://www.pensanoevento.com.br/baladas/", "cl": "Baladas"},
    {"url": "https://www.pensanoevento.com.br/shows/", "cl": "Shows"},
]

for category in categories:
    extractData(category["url"], category["cl"])
