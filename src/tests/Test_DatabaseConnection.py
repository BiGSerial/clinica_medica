# src/tests/Test_DatabaseConnection.py
import sys
sys.path.append('.')

import unittest
from src.database.Database import DatabaseConnection
import cx_Oracle

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
            self.assertIsNotNone(self.db.connection, "A conexão não foi estabelecida corretamente.")
        except Exception as e:
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
            self.assertIsNone(self.db.connection, "A conexão não foi fechada corretamente.")
        except Exception as e:
            self.fail(f"Falha ao desconectar do banco de dados: {e}")

    def test_get_cursor(self):
        """
        Testa se o cursor é retornado corretamente após a conexão.
        """
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            self.assertIsNotNone(cursor, "Falha ao obter o cursor.")
        except Exception as e:
            self.fail(f"Falha ao obter o cursor do banco de dados: {e}")
        finally:
            self.db.disconnect()

    def test_execute_simple_query(self):
        """
        Testa a execução de uma consulta simples no banco de dados.
        """
        cursor = None  # Inicializa a variável cursor
        
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            # Executa uma consulta simples (por exemplo, lista de tabelas)
            cursor.execute("SELECT table_name FROM user_tables")
            tables = cursor.fetchall()

            # Verifica se o resultado não está vazio
            self.assertIsInstance(tables, list, "O resultado da consulta não é uma lista.")
            self.assertGreater(len(tables), 0, "Nenhuma tabela foi encontrada no banco de dados.")

        except cx_Oracle.DatabaseError as e:
            self.fail(f"Erro ao executar consulta: {e}")
        finally:
            if cursor:
                cursor.close()
            self.db.disconnect()

    def tearDown(self):
        """
        Limpeza após cada teste.
        Garante que a conexão seja fechada.
        """
        if self.db.connection:
            self.db.disconnect()

if __name__ == '__main__':
    unittest.main()
