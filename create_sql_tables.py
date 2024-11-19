import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

engine = create_engine(
    f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

def get_engine():
    return engine

def criar_tabelas():
    criar_tabelas_sql = """
    CREATE TABLE IF NOT EXISTS eventos (
        id_evento SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        tipo VARCHAR(100) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS dados_eventos (
        id_dado SERIAL PRIMARY KEY,
        id_evento INTEGER REFERENCES eventos(id_evento) ON DELETE CASCADE,
        data_evento VARCHAR(255) NOT NULL,
        localizacao VARCHAR(255) NOT NULL,
        address TEXT
    );

    CREATE TABLE IF NOT EXISTS metadados (
        id_metadado SERIAL PRIMARY KEY,
        id_evento INTEGER REFERENCES eventos(id_evento) ON DELETE CASCADE,
        event_link VARCHAR(255),
        event_photo VARCHAR(255)
    );
    """

    with engine.connect() as connection:
        connection.execute(text(criar_tabelas_sql))
        connection.execute(text("COMMIT;"))
        print("Tabelas criadas com sucesso!")

def insert_evento(nome, tipo):
    with engine.connect() as connection:
        result = connection.execute(
            text("INSERT INTO eventos (nome, tipo) VALUES (:nome, :tipo) RETURNING id_evento"),
            {"nome": nome, "tipo": tipo}
        )
        connection.execute(text("COMMIT;"))
        return result.fetchone()[0]

def insert_dados_evento(id_evento, data_evento, localizacao, address):
    with engine.connect() as connection:
        connection.execute(
            text("INSERT INTO dados_eventos (id_evento, data_evento, localizacao, address) VALUES (:id_evento, :data_evento, :localizacao, :address)"),
            {"id_evento": id_evento, "data_evento": data_evento, "localizacao": localizacao, "address": address}
        )
        connection.execute(text("COMMIT;"))

def insert_metadados(id_evento, event_link, event_photo):
    with engine.connect() as connection:
        connection.execute(
            text("INSERT INTO metadados (id_evento, event_link, event_photo) VALUES (:id_evento, :event_link, :event_photo)"),
            {"id_evento": id_evento, "event_link": event_link, "event_photo": event_photo}
        )
        connection.execute(text("COMMIT;"))

criar_tabelas()