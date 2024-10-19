import sys
sys.path.append('.')

from src.database.Database import DatabaseConnection
from src.app.models.especialidades import Especialidades

class EspecialidadesController:
    def __init__(self):
        self.db = DatabaseConnection()

    def criar_especialidade(self, especialidade: Especialidades):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''INSERT INTO especialidades (id_especialidade, nome_especialidade)
                     VALUES (:id_especialidade, :nome_especialidade)'''
            
            cursor.execute(sql, {
                'id_especialidade': especialidade.getIdEspecialidade(),
                'nome_especialidade': especialidade.getNomeEspecialidade()
            })
            

            especialidade.setIdEspecialidade(cursor.lastrowid)
            
            if self.db.connection:
                self.db.connection.commit()
                print("Especialidade criada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao criar especialidade: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()

    def buscar_especialidade(self, id_especialidade):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            
            sql = "SELECT * FROM especialidades WHERE id_especialidade = :id_especialidade"
            cursor.execute(sql, {'id_especialidade': id_especialidade})
            especialidade = cursor.fetchone()
            
            if especialidade:
                return Especialidades(
                    nome_especialidade=especialidade[0]
                )
            else:
                print("Especialidade não encontrada.")
        
        except Exception as e:
            print(f"Erro ao buscar especialidade: {e}")
            return None
        
        finally:
            self.db.disconnect()

    def atualizar_especialidade(self, especialidade: Especialidades):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''UPDATE especialidades SET 
                     nome_especialidade = :nome_especialidade
                     WHERE id_especialidade = :id_especialidade'''
            
            cursor.execute(sql, {
                'nome_especialidade': especialidade.getNomeEspecialidade(),
                'id_especialidade': especialidade.getIdEspecialidade()
            })
            
            if self.db.connection:
                self.db.connection.commit()
                print("Especialidade atualizada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao atualizar especialidade: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()

    def deletar_especialidade(self, id_especialidade):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = "DELETE FROM especialidades WHERE id_especialidade = :id_especialidade"
            cursor.execute(sql, {'id_especialidade': id_especialidade})
            
            if self.db.connection:
                self.db.connection.commit()
                print("Especialidade deletada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao deletar especialidade: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()
