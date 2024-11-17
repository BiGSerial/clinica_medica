# src/database/Database.py
import sys
sys.path.append('.')

import pymongo
from src.config.Config import Config
import logging

class DatabaseConnection:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        """
        Estabelece a conexão com o banco de dados MongoDB.
        """
        try:
            connection_string = Config.get_connection_string()
            self.client = pymongo.MongoClient(connection_string)
            self.db = self.client.get_database()
            if self.client.is_primary:  # Verifica se o cliente está conectado corretamente
                logging.info("Conexão com o banco de dados MongoDB estabelecida.")
            else:
                logging.error("A conexão não foi estabelecida corretamente.")
                raise pymongo.errors.ConnectionFailure("Não foi possível estabelecer a conexão com o servidor MongoDB.")
        except pymongo.errors.ServerSelectionTimeoutError as e:
            logging.error(f"Erro ao conectar ao banco de dados MongoDB: {e}")
            raise


    def disconnect(self):
        """
        Fecha a conexão com o banco de dados MongoDB se ela estiver ativa.
        """
        if self.client:
            try:
                self.client.close()
                self.client = None
                self.db = None
                logging.info("Conexão com o banco de dados MongoDB fechada.")
            except pymongo.errors.ServerSelectionTimeoutError as e:
                logging.error(f"Erro ao fechar a conexão com o banco de dados MongoDB: {e}")
                raise
        else:
            logging.warning("Nenhuma conexão ativa para fechar.")

    def get_collection(self, collection_name):
        """
        Retorna uma coleção para realizar operações no banco.
        """
        if self.db:
            try:
                return self.db[collection_name]
            except pymongo.errors.PyMongoError as e:
                logging.error(f"Erro ao obter a coleção: {e}")
                raise
        else:
            raise Exception("Conexão com o banco de dados MongoDB não estabelecida.")

    def get_cursor(self):
        """
        Retorna um cursor de uma coleção para realizar operações.
        """
        # Exemplo de como pegar um cursor de uma coleção. Ajuste conforme necessário
        if self.db:
            try:
                collection = self.db['example_collection']
                return collection.find()  # Retorna um cursor
            except pymongo.errors.PyMongoError as e:
                logging.error(f"Erro ao obter o cursor: {e}")
                raise
        else:
            raise Exception("Conexão com o banco de dados MongoDB não estabelecida.")
