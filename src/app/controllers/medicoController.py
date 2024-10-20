import sys
sys.path.append('.')

from src.database.Database import DatabaseConnection
from src.app.models.medico import Medico
import cx_Oracle

class MedicoController:
    def __init__(self):
        self.db = DatabaseConnection()

    def criar_medico(self, medico: Medico):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''INSERT INTO medicos 
                     (nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade) 
                     VALUES (:nome, :crm, :telefone, :email, :cep, :data_nascimento, :data_contratacao, :data_registro, :id_especialidade)
                     RETURNING id_medico INTO :id_medico'''
            
            id_medico_var = cursor.var(int)
            cursor.execute(sql, {
                'nome': medico.getNome(),
                'crm': medico.getCrm(),
                'telefone': medico.getTelefone(),
                'email': medico.getEmail(),
                'cep': medico.getCep(),
                'data_nascimento': medico.getDataNascimento(),
                'data_contratacao': medico.getDataContratacao(),
                'data_registro': medico.getDataRegistro(),
                'id_especialidade': medico.getIdEspecialidade(),
                'id_medico': id_medico_var
            })

            medico.setIdMedico(id_medico_var.getvalue()[0]) 

            if self.db.connection:
                self.db.connection.commit()
                print("Médico criado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao criar médico: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()

    def buscar_medico_por_nome(self, nome_parcial):
        """
        Busca médicos cujo nome contenha a string parcial fornecida.
        """
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = """
                SELECT m.id_medico, m.crm, m.nome, e.nome_especialidade 
                FROM medicos m
                JOIN especialidades e ON m.id_especialidade = e.id_especialidade
                WHERE LOWER(m.nome) LIKE LOWER(:nome_parcial)
            """
            cursor.execute(sql, {'nome_parcial': f'%{nome_parcial}%'})
            medicos = cursor.fetchall()

            return medicos
        
        except Exception as e:
            print(f"Erro ao buscar médicos por nome parcial: {e}")
            return []
        
        finally:
            self.db.disconnect()

    def buscar_medico(self, id_medico):
        """
        Busca um médico por ID.
        """
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = """
                SELECT m.id_medico, m.crm, m.nome, e.nome_especialidade 
                FROM medicos m
                JOIN especialidades e ON m.id_especialidade = e.id_especialidade
                WHERE m.id_medico = :id_medico
            """
            cursor.execute(sql, {'id_medico': id_medico})
            medico = cursor.fetchone()

            return medico
        
        except Exception as e:
            print(f"Erro ao buscar médico: {e}")
            return None
        
        finally:
            self.db.disconnect()

    def atualizar_medico(self, medico: Medico):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''UPDATE medicos SET 
                     nome = :nome,
                     crm = :crm, 
                     telefone = :telefone,
                     email = :email,
                     cep = :cep,
                     data_nascimento = :data_nascimento,
                     data_contratacao = :data_contratacao,
                     data_registro = :data_registro,
                     id_especialidade = :id_especialidade
                     WHERE id_medico = :id_medico'''
            
            cursor.execute(sql, {
                'nome': medico.getNome(),
                'crm': medico.getCrm(),
                'telefone': medico.getTelefone(),
                'email': medico.getEmail(),
                'cep': medico.getCep(),
                'data_nascimento': medico.getDataNascimento(),
                'data_contratacao': medico.getDataContratacao(),
                'data_registro': medico.getDataRegistro(),
                'id_especialidade': medico.getIdEspecialidade(),
                'id_medico': medico.getIdMedico()
            })
            
            if self.db.connection:
                self.db.connection.commit()
                print("Médico atualizado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao atualizar médico: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()


    def listar_todos_medicos(self):
        """
        Retorna uma lista com todos os médicos e suas especialidades.
        """
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = """
                SELECT m.id_medico, m.crm, m.nome, e.nome_especialidade 
                FROM medicos m
                JOIN especialidades e ON m.id_especialidade = e.id_especialidade
            """
            cursor.execute(sql)
            medicos = cursor.fetchall()

            return medicos
        
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")
            return []
        
        finally:
            self.db.disconnect()


    def deletar_medico(self, id_medico):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = "DELETE FROM medicos WHERE id_medico = :id_medico"
            cursor.execute(sql, {'id_medico': id_medico})
            
            if self.db.connection:
                self.db.connection.commit()
                print("Médico deletado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao deletar médico: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()
