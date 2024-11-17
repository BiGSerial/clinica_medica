# src/tests/Test_DatabaseConnection.py
import sys
sys.path.append('.')

import unittest
from src.database.Database import DatabaseConnection
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        """
        Configuração antes de cada teste.
        Inicializa a classe DatabaseConnection e conecta ao banco de dados.
        """
        self.db = DatabaseConnection()

    def test_connect(self):
        """
        Testa se a conexão com o banco de dados é estabelecida corretamente.
        """
        try:
            self.db.connect()
            self.assertIsNotNone(self.db.client, "A conexão não foi estabelecida corretamente.")
        except ConnectionFailure as e:
            self.fail(f"Falha ao conectar ao banco de dados: {e}")
        finally:
            self.db.disconnect()

    def test_disconnect(self):
        """
        Testa se a desconexão com o banco de dados ocorre corretamente.
        """
        try:
            self.db.connect()
            self.db.disconnect()
            self.assertIsNone(self.db.client, "A conexão não foi fechada corretamente.")
        except ConnectionFailure as e:
            self.fail(f"Falha ao desconectar do banco de dados: {e}")

    def test_get_collection(self):
        """
        Testa se a coleção é retornada corretamente após a conexão.
        """
        try:
            self.db.connect()
            collection = self.db.get_collection('example_collection')

            # Verifique se a coleção realmente existe no banco de dados
            self.assertIn('example_collection', self.db.list_collection_names(), "A coleção 'example_collection' não existe.")
        except ConnectionFailure as e:
            self.fail(f"Falha ao obter a coleção do banco de dados: {e}")
        finally:
            self.db.disconnect()


    def test_execute_simple_query(self):
        """
        Testa a execução de uma consulta simples no banco de dados.
        """
        collection = None  # Inicializa a variável collection
        
        try:
            self.db.connect()
            collection = self.db.get_collection('medicos')

            # Executa uma consulta simples (por exemplo, lista de documentos)
            documents = collection.find()

            # Verifica se o resultado não está vazio
            self.assertIsInstance(documents, pymongo.cursor.Cursor, "O resultado da consulta não é um cursor.")
            # Você pode adicionar verificações de quantidade de documentos dependendo do que tiver na coleção

        except ConnectionFailure as e:
            self.fail(f"Erro ao executar consulta: {e}")
        finally:
            if collection:
                collection.close()  # Se necessário, feche a coleção
            self.db.disconnect()

    def tearDown(self):
        """
        Limpeza após cada teste.
        Garante que a conexão seja fechada.
        """
        if self.db.client:
            self.db.disconnect()
