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

print("\n2. Mostrar os dados dos 2 eventos mais próximos de iniciar:")
query_listar_dois_eventos_mais_proximos = """
          SELECT * 
          FROM dados_eventos
          ORDER BY data_evento ASC
          LIMIT 2
          """
consultar(query_listar_dois_eventos_mais_proximos)

print("\n3. Mostrar os eventos que acontecem em Florianópolis/SC:")
query_listar_eventos_florianopolis = """
          SELECT * 
          FROM dados_eventos 
          WHERE endereco LIKE '%Florianópolis/SC%'
          """
consultar(query_listar_eventos_florianopolis)

print("\n4. Mostrar todos os eventos que são ao ar livre:")
print("Para essa questão, como não há categoria de 'Ar livre', procurei por localizações que contenham 'Praças', 'Praça' e 'Praia'")
query_listar_eventos_ar_livre = """
            SELECT * 
            FROM dados_eventos 
            WHERE LOWER(localizacao) LIKE '%praça%' 
            OR LOWER(localizacao) LIKE '%praças%' 
            OR LOWER(localizacao) LIKE '%praia%'
          """
consultar(query_listar_eventos_ar_livre)

print("\n5. Mostrar todos os Metadados por evento:")
query_metadados = """
            SELECT * 
            FROM metadados
          """
consultar(query_metadados)
