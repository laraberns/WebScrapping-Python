import requests

def extractData():
    base_url = 'https://destinopoa.com.br/calendario/'
    headers = {
        'User-Agent': 'Chrome/114.0.0.0'
    }
    
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        print("Requisição bem-sucedida!")
        print(response.text) 
    else:
        print(f"Erro: {response.status_code}")

extractData()
