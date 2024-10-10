# src/database/Database.py
import cx_Oracle
from src.config.Config import Config
import logging

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        """
        Estabelece a conexão com o banco de dados.
        """
        try:
            connection_string = Config.get_connection_string()
            self.connection = cx_Oracle.connect(connection_string)
            logging.info("Conexão com o banco de dados estabelecida.")
        except cx_Oracle.DatabaseError as e:
            logging.error(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def disconnect(self):
        """
        Fecha a conexão com o banco de dados se ela estiver ativa.
        """
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
                logging.info("Conexão com o banco de dados fechada.")
            except cx_Oracle.DatabaseError as e:
                logging.error(f"Erro ao fechar a conexão com o banco de dados: {e}")
                raise
        else:
            logging.warning("Nenhuma conexão ativa para fechar.")

    def get_cursor(self):
        """
        Retorna um cursor para realizar operações no banco.
        """
        if self.connection:
            try:
                return self.connection.cursor()
            except cx_Oracle.DatabaseError as e:
                logging.error(f"Erro ao obter o cursor: {e}")
                raise
        else:
            raise Exception("Conexão com o banco de dados não estabelecida.")
