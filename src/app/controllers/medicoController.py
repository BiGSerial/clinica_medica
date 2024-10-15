# src/app/controllers/medicoController.py

from src.database.Database import DatabaseConnection
from src.app.models.medico import Medico

class MedicoController:
    def __init__(self):
        self.db = DatabaseConnection()

    def criar_medico(self, medico: Medico):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''INSERT INTO medicos 
                     (nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade) 
                     VALUES (:nome, :crm, :telefone, :email, :cep, :data_nascimento, :data_contratacao, :data_registro, :id_especialidade)'''
            
            cursor.execute(sql, {
                'nome': medico.getNome(),
                'crm': medico.getCrm(),
                'telefone': medico.getTelefone(),
                'email': medico.getEmail(),
                'cep': medico.getCep(),
                'data_nascimento': medico.getDataNascimento(),
                'data_contratacao': medico.getDataContratacao(),
                'data_registro': medico.getDataRegistro(),
                'id_especialidade': medico.getIdEspecialidade()
            })

            #Pega o id do médico criado
            medico.setIdMedico(cursor.lastrowid)
            
            if self.db.connection:
                self.db.connection.commit()
                print("Médico criado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao criar médico: {e}")
        
        finally:
            self.db.disconnect()

    def buscar_medico(self, id_medico):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            
            sql = "SELECT * FROM medicos WHERE id_medico = :id_medico"
            cursor.execute(sql, {'id_medico': id_medico})
            medico = cursor.fetchone()
            
            if medico:
                return Medico(
                    nome=medico[1],
                    crm=medico[2],
                    telefone=medico[3],
                    email=medico[4],
                    cep=medico[5],
                    data_nascimento=medico[6],
                    data_contratacao=medico[7],
                    data_registro=medico[8],
                    id_especialidade=medico[9]
                )

            else:
                print("Médico não encontrado.")
        
        except Exception as e:
            print(f"Erro ao buscar médico: {e}")
        
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
        
        finally:
            self.db.disconnect()
