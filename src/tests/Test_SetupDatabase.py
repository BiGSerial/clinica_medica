# src/tests/Test_SetupDatabase.py
from src.database.Database import DatabaseConnection

def setup_tables():
    db = DatabaseConnection()
    db.connect()
    cursor = db.get_cursor()

    try:
        # Lê o arquivo SQL e executa os comandos
        with open('src/database/setup.sql', 'r') as file:
            sql_script = file.read()
            sql_commands = sql_script.split(';')  # Separar os comandos por ';'
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

        # Verifica se a conexão não é None antes de fazer commit
        if db.connection:
            db.connection.commit()

    except Exception as e:
        print(f"Erro ao configurar as tabelas: {e}")
    
    finally:
        # Sempre feche o cursor e a conexão, mesmo que ocorra um erro
        if cursor:
            cursor.close()
        if db.connection:
            db.disconnect()

if __name__ == "__main__":
    setup_tables()
