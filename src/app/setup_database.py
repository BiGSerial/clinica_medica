# src/app/setup_database.py
import sys
sys.path.append('.')

from src.database.Database import DatabaseConnection

def setup_tables():
    db = DatabaseConnection()
    try:
        db.connect()
        cursor = db.get_cursor()

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
