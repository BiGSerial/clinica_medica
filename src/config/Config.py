# src/config/Config.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

class Config:
    
    @staticmethod
    def get_connection_string():
        # Carregar variáveis do arquivo .env
        load_dotenv()

        # Obter as variáveis de ambiente
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')

        # Retornar a string de conexão
        return f"mongodb://{db_host}:{db_port}/{db_name}"

    @staticmethod
    def get_mongo_client():
        connection_string = Config.get_connection_string()
        return MongoClient(connection_string)
