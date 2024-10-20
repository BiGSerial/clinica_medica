import sys
sys.path.append('.')

from src.database.Database import DatabaseConnection
from src.app.models.especialidades import Especialidades
import cx_Oracle

class EspecialidadesController:
    def __init__(self):
        self.db = DatabaseConnection()

    def criar_especialidade(self, especialidade: Especialidades):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''INSERT INTO especialidades (nome_especialidade)
                     VALUES (:nome_especialidade)
                     RETURNING id_especialidade INTO :id_especialidade'''
            
            id_especialidade_var = cursor.var(int)  # Variável para capturar o ID gerado
            cursor.execute(sql, {
                'nome_especialidade': especialidade.getNomeEspecialidade(),
                'id_especialidade': id_especialidade_var
            })

            especialidade.setIdEspecialidade(id_especialidade_var.getvalue()[0])  # Define o ID gerado

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
                    nome_especialidade=especialidade[1],
                    id_especialidade=especialidade[0]
                )
            else:
                print("Especialidade não encontrada.")
                return None
        
        except Exception as e:
            print(f"Erro ao buscar especialidade: {e}")
        
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

    def listar_todas_especialidades(self):
        """
        Retorna uma lista com todas as especialidades cadastradas no banco de dados.
        """
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = "SELECT * FROM especialidades"
            cursor.execute(sql)
            especialidades = cursor.fetchall()

            lista_especialidades = []
            for esp in especialidades:
                especialidade = Especialidades(esp[1])
                especialidade.setIdEspecialidade(esp[0])
                lista_especialidades.append(especialidade)

            return lista_especialidades
        
        except Exception as e:
            print(f"Erro ao listar especialidades: {e}")
            return []
        
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
