# src/tests/Test_DatabaseCRUD.py
import unittest
from src.database.Database import DatabaseConnection
import cx_Oracle

class TestDatabaseCRUD(unittest.TestCase):

    def setUp(self):
        """
        Configuração antes de cada teste.
        Inicializa a classe DatabaseConnection e conecta ao banco de dados.
        """
        self.db = DatabaseConnection()
        self.db.connect()
        self.cursor = self.db.get_cursor()

    def test_insert_especialidade(self):
        """
        Testa a inserção de uma nova especialidade.
        """
        try:
            # Inserir uma especialidade
            self.cursor.execute("""
                INSERT INTO ESPECIALIDADES (NOME_ESPECIALIDADE)
                VALUES (:nome_especialidade)""", {'nome_especialidade': 'Cardiologia'})

            # Verificar se a conexão está ativa antes de fazer commit
            if self.db.connection:
                self.db.connection.commit()

            # Verificar se a inserção foi realizada
            self.cursor.execute("SELECT * FROM ESPECIALIDADES WHERE NOME_ESPECIALIDADE = :nome", {'nome': 'Cardiologia'})
            result = self.cursor.fetchone()

            self.assertIsNotNone(result, "Falha ao inserir especialidade.")
            self.assertEqual(result[1], 'Cardiologia', "O nome da especialidade inserida não confere.")

        except cx_Oracle.DatabaseError as e:
            self.fail(f"Falha ao inserir especialidade: {e}")

    def test_update_especialidade(self):
        """
        Testa a atualização de uma especialidade existente.
        """
        try:
            # Inserir uma especialidade para atualizar
            self.cursor.execute("""
                INSERT INTO ESPECIALIDADES (NOME_ESPECIALIDADE)
                VALUES (:nome_especialidade)""", {'nome_especialidade': 'Neurologia'})

            # Verificar se a conexão está ativa antes de fazer commit
            if self.db.connection:
                self.db.connection.commit()

            # Atualizar o nome da especialidade
            self.cursor.execute("""
                UPDATE ESPECIALIDADES
                SET NOME_ESPECIALIDADE = :novo_nome
                WHERE NOME_ESPECIALIDADE = :nome_atual""",
                {'novo_nome': 'Neurocirurgia', 'nome_atual': 'Neurologia'})

            # Verificar se a conexão está ativa antes de fazer commit
            if self.db.connection:
                self.db.connection.commit()

            # Verificar se a atualização foi realizada
            self.cursor.execute("SELECT * FROM ESPECIALIDADES WHERE NOME_ESPECIALIDADE = :nome", {'nome': 'Neurocirurgia'})
            result = self.cursor.fetchone()

            self.assertIsNotNone(result, "Falha ao atualizar a especialidade.")
            self.assertEqual(result[1], 'Neurocirurgia', "A especialidade não foi atualizada corretamente.")

        except cx_Oracle.DatabaseError as e:
            self.fail(f"Falha ao atualizar especialidade: {e}")

    def test_delete_especialidade(self):
        """
        Testa a exclusão de uma especialidade.
        """
        try:
            # Inserir uma especialidade para deletar
            self.cursor.execute("""
                INSERT INTO ESPECIALIDADES (NOME_ESPECIALIDADE)
                VALUES (:nome_especialidade)""", {'nome_especialidade': 'Oncologia'})

            # Verificar se a conexão está ativa antes de fazer commit
            if self.db.connection:
                self.db.connection.commit()

            # Deletar a especialidade
            self.cursor.execute("DELETE FROM ESPECIALIDADES WHERE NOME_ESPECIALIDADE = :nome", {'nome': 'Oncologia'})

            # Verificar se a conexão está ativa antes de fazer commit
            if self.db.connection:
                self.db.connection.commit()

            # Verificar se a exclusão foi realizada
            self.cursor.execute("SELECT * FROM ESPECIALIDADES WHERE NOME_ESPECIALIDADE = :nome", {'nome': 'Oncologia'})
            result = self.cursor.fetchone()

            self.assertIsNone(result, "Falha ao deletar a especialidade.")
        
        except cx_Oracle.DatabaseError as e:
            self.fail(f"Falha ao deletar especialidade: {e}")

    def tearDown(self):
        """
        Limpeza após cada teste.
        Garante que a conexão seja fechada.
        """
        if self.cursor:
            self.cursor.close()
        self.db.disconnect()

if __name__ == '__main__':
    unittest.main()
