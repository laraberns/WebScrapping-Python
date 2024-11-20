from datetime import datetime

def format_event_date(event_date_str):
    """Converte a string da data do evento para o formato date."""
    try:
        event_date_str = event_date_str.split(" - ")[1]
        
        event_date = datetime.strptime(event_date_str, "%d.%m.%Y").date()
        return event_date
    except Exception as e:
        print(f"Erro ao formatar a data: {e}")
        return None
