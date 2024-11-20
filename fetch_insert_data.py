import requests
from bs4 import BeautifulSoup
from create_sql_tables import insert_evento, insert_dados_evento, insert_metadados
from format_date import format_event_date

def extract_event_details(event_link):
    """Extrai detalhes adicionais de uma página individual do evento."""
    response = requests.get(event_link)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extrai o endereço do evento (pega o segundo parágrafo com a classe 'card-text')
        event_address_elements = soup.find_all("p", class_="card-text")
        event_address = event_address_elements[1].text.strip() if len(event_address_elements) > 1 else "Sem endereço"

        # Remove a parte "Como chegar?" do endereço, caso presente
        if "Como chegar?" in event_address:
            event_address = event_address.split("Como chegar?")[0].strip()

        # Extrai a categoria do evento (se existir)
        category = soup.find("span", class_="text-muted badge badge-outline small")
        category = category.text.strip() if category else "Sem categoria"
        
        return event_address, category
    else:
        # Caso haja erro na requisição, imprime o código de erro e retorna valores padrão
        print(f"Error fetching event details: {response.status_code} for {event_link}")
        return "Sem endereço", "Sem categoria"

def extractData(url):
    """Extrai dados dos eventos da página principal e dos detalhes de cada evento."""
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all("div", class_="card shadow")
        
        for card in cards:
            event_name = card.find("p", class_="card-text")
            event_name = event_name.text.strip() if event_name else "Sem nome" 
            
            # Extrai a data e converte para o formato desejado
            event_date_raw = card.find("div", class_="card-title")
            event_date_raw = event_date_raw.text.strip() if event_date_raw else "Sem data"
            event_date = format_event_date(event_date_raw)
            
            event_place = card.find("span", class_="text-muted")
            event_place = event_place.text.strip() if event_place else "Sem local" 

            event_link = card.find("a", class_="text-dark font-weight-bold text-decoration-none stretched-link")
            event_link = event_link['href'] if event_link else None
            
            event_photo = card.find("img", class_="card-img-top border-bottom")
            event_photo = event_photo['src'] if event_photo else "Sem foto"  
            
            if event_link:
                event_address, category = extract_event_details(event_link)
            else:
                event_address, category = "Sem endereço", "Sem categoria"  

            # Passa os dados extraídos para a função de inserção no banco de dados
            evento_id = insert_evento(event_name, category)
            insert_dados_evento(evento_id, event_date, event_place, event_address)
            insert_metadados(evento_id, event_link, event_photo)

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

    """Extrai dados dos eventos da página principal e dos detalhes de cada evento."""
    response = requests.get(url)

# Chama a função com a URL principal de eventos
extractData("https://www.pensanoevento.com.br/eventos/")
