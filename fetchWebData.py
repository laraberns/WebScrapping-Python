import requests
from bs4 import BeautifulSoup

def extractData(url, category):
    for page in range(1, 4):  # Itera pelas 3 primeiras páginas
        page_url = f"{url}&page={page}"  # Atualiza a URL para a página atual
        response = requests.get(page_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all("div", class_="CustomGridstyle__CustomGridCardType-sc-1ce1n9e-2")
            
            for card in cards:
                # Extract Event Name
                event_name = card.find("h3", class_="EventCardstyle__EventTitle-sc-1rkzctc-7")
                event_name = event_name.text.strip() if event_name else "No name found"
                
                # Extract Event Date
                event_date = card.find("div", class_="EventCardstyle__EventDate-sc-1rkzctc-6")
                event_date = event_date.text.strip() if event_date else "No date found"
                
                # Extract Event Address 
                event_address = card.find("div", class_="EventCardstyle__EventLocation-sc-1rkzctc-8")
                event_address = event_address.text.strip() if event_address else "No address found"
                
                # Print the extracted data along with category
                print(f"Category: {category}")
                print(f"Event Name: {event_name}")
                print(f"Event Date: {event_date}")
                print(f"Event Address: {event_address}")
                print("-" * 40)
        else:
            print(f"Error: {response.status_code} on page {page} of {category}")

categories = [
    {"url": "https://www.sympla.com.br/eventos/florianopolis-sc/todos-eventos?cl=1-gastronomia", "cl": "Gastronomia"},
    {"url": "https://www.sympla.com.br/eventos/florianopolis-sc/todos-eventos?cl=8-curso-e-workshops", "cl": "Curso e Workshops"},
    {"url": "https://www.sympla.com.br/eventos/florianopolis-sc/todos-eventos?cl=17-festas-e-shows", "cl": "Festas e Shows"},
    {"url": "https://www.sympla.com.br/eventos/florianopolis-sc/todos-eventos?cl=4-congressos-e-palestras", "cl": "Congressos e palestras"}
]

for category in categories:
    extractData(category["url"], category["cl"])
