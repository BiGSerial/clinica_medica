import sys
import cx_Oracle
sys.path.append('.')

from src.database.Database import DatabaseConnection

def drop_table_if_exists(cursor, table_name):
    """
    Função para tentar dropar uma tabela, ignorando o erro se a tabela não existir.
    """
    try:
        cursor.execute(f"DROP TABLE {table_name} CASCADE CONSTRAINTS")
        print(f"Tabela {table_name} removida com sucesso.")
    except cx_Oracle.DatabaseError as e:
        error_obj, = e.args
        if error_obj.code == 942:  # ORA-00942: table or view does not exist
            print(f"Tabela {table_name} não existe. Ignorando.")
        else:
            raise

def setup_tables():
    db = DatabaseConnection()
    try:
        db.connect()
        cursor = db.get_cursor()

        # Tentar dropar as tabelas se existirem
        drop_table_if_exists(cursor, 'CONSULTAS')
        drop_table_if_exists(cursor, 'MEDICOS')
        drop_table_if_exists(cursor, 'PACIENTES')
        drop_table_if_exists(cursor, 'ESPECIALIDADES')

        # Lê o arquivo SQL e executa os comandos
        with open('src/database/setup.sql', 'r') as file:
            sql_script = file.read()
            sql_commands = sql_script.split(';')  # Separar os comandos por ';'
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

        print("Tabelas criadas com sucesso.")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        db.disconnect()

if __name__ == "__main__":
    setup_tables()
