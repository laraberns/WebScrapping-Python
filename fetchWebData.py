import requests
from bs4 import BeautifulSoup
from sql_actions import insert_evento, insert_dados_evento, insert_metadados

def extract_event_details(event_link):
    """Extrai detalhes adicionais de uma página individual do evento."""
    response = requests.get(event_link)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract Event Address (pegar o segundo card-text)
        event_address_elements = soup.find_all("p", class_="card-text")
        event_address = event_address_elements[1].text.strip() if len(event_address_elements) > 1 else "No address found"

        # Remove "Como chegar?" se presente no endereço
        if "Como chegar?" in event_address:
            event_address = event_address.split("Como chegar?")[0].strip()

        # Extract Category
        category = soup.find("span", class_="text-muted badge badge-outline small")
        category = category.text.strip() if category else "No category found"
        
        return event_address, category
    else:
        print(f"Error fetching event details: {response.status_code} for {event_link}")
        return "No address found", "No category found"

def extractData(url):
    """Extrai dados dos eventos da página principal e dos detalhes de cada evento."""
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
            event_link = event_link['href'] if event_link else None
            
            # Extract Event Photo
            event_photo = card.find("img", class_="card-img-top border-bottom")
            event_photo = event_photo['src'] if event_photo else "No photo found"
            
            # If event link is present, fetch additional details
            if event_link:
                event_address, category = extract_event_details(event_link)
            else:
                event_address, category = "No address found", []

            # Pass the extracted data to insert into database
            evento_id = insert_evento(event_name, category)
            insert_dados_evento(evento_id, event_date, event_place, event_address)
            insert_metadados(evento_id, event_link, event_photo)

            # Print the extracted data
            print(f"Event Name: {event_name}")
            print(f"Event Date: {event_date}")
            print(f"Event Place: {event_place}")
            print(f"Event Address: {event_address}")
            print(f"Category: {category}")
            print(f"Event Link: {event_link}")
            print(f"Event Photo: {event_photo}")
            print("-" * 40)
    else:
        print(f"Error: {response.status_code} for URL {url}")

# Chamar a função com a URL principal
extractData("https://www.pensanoevento.com.br/eventos/")
