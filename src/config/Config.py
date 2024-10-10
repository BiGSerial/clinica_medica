# src/config/Config.py
import os
from dotenv import load_dotenv

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
        db_service = os.getenv('DB_SERVICE')

        # Retornar a string de conexão
        return f"{db_user}/{db_password}@{db_host}:{db_port}/{db_service}"
