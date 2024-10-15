# src/app/controllers/pacienteController.py

from src.database.Database import DatabaseConnection
from src.app.models.paciente import Paciente

class PacienteController:
    def __init__(self):
        self.db = DatabaseConnection()

    def criar_paciente(self, paciente: Paciente):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''INSERT INTO pacientes 
                     (nome, cpf, sexo, email, cep, data_nascimento, telefone) 
                     VALUES (:nome, :cpf, :sexo, :email, :cep, :data_nascimento, :telefone)'''
            
            cursor.execute(sql, {
                'nome': paciente.getNome(),
                'cpf': paciente.getCpf(),
                'sexo': paciente.getSexo(),
                'email': paciente.getEmail(),
                'cep': paciente.getCep(),
                'data_nascimento': paciente.getDataNascimento(),
                'telefone': paciente.getTelefone()
            })

            #Pega o id do paciente criado
            paciente.setIdPaciente(cursor.lastrowid)
            
            if self.db.connection:
                self.db.connection.commit()
                print("Paciente criado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao criar paciente: {e}")
        
        finally:
            self.db.disconnect()

    def buscar_paciente(self, id_paciente):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            
            sql = "SELECT * FROM pacientes WHERE id_paciente = :id_paciente"
            cursor.execute(sql, {'id_paciente': id_paciente})
            paciente = cursor.fetchone()
            
            if paciente:
                return Paciente(
                    id_paciente=paciente[0],
                    nome=paciente[1],
                    cpf=paciente[2],
                    sexo=paciente[3],
                    email=paciente[4],
                    cep=paciente[5],
                    data_nascimento=paciente[6],
                    telefone=paciente[7]
                )
            else:
                print("Paciente não encontrado.")
        
        except Exception as e:
            print(f"Erro ao buscar paciente: {e}")
        
        finally:
            self.db.disconnect()

    def atualizar_paciente(self, paciente: Paciente):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''UPDATE pacientes SET 
                     nome = :nome,
                     cpf = :cpf, 
                     sexo = :sexo,
                     email = :email,
                     cep = :cep,
                     data_nascimento = :data_nascimento,
                     telefone = :telefone
                     WHERE id_paciente = :id_paciente'''
            
            cursor.execute(sql, {
                'nome': paciente.getNome(),
                'cpf': paciente.getCpf(),
                'sexo': paciente.getSexo(),
                'email': paciente.getEmail(),
                'cep': paciente.getCep(),
                'data_nascimento': paciente.getDataNascimento(),
                'telefone': paciente.getTelefone(),
                'id_paciente': paciente.getIdPaciente()
            })
            
            if self.db.connection:
                self.db.connection.commit()
                print("Paciente atualizado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")
        
        finally:
            self.db.disconnect()

    def deletar_paciente(self, id_paciente):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = "DELETE FROM pacientes WHERE id_paciente = :id_paciente"
            cursor.execute(sql, {'id_paciente': id_paciente})
            
            if self.db.connection:
                self.db.connection.commit()
                print("Paciente deletado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao deletar paciente: {e}")
        
        finally:
            self.db.disconnect()
