import pandas as pd
from sqlalchemy import text
from create_sql_tables import get_engine

# Função de consulta dinâmica
def consultar(query):
    engine = get_engine()
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df)

# Consultas
print("1. Mostrar todos os eventos com suas datas, localização, e tipo de evento:")
query_listar_eventos = """
          SELECT eventos.nome, dados_eventos.data_evento, dados_eventos.localizacao, eventos.tipo
          FROM eventos
          INNER JOIN dados_eventos ON eventos.id_evento = dados_eventos.id_evento
          """
consultar(query_listar_eventos)
