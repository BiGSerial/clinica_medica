from pymongo import MongoClient
from bson.objectid import ObjectId
from src.app.models.paciente import Paciente

class PacienteController:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['clinicadb']
        self.collection = self.db['pacientes']

    def criar_paciente(self, paciente: Paciente):
        try:
            # Recupera o último ID usado na coleção, ordenando por id_paciente
            last_paciente = self.collection.find_one(sort=[("id_paciente", -1)])
            new_id = (last_paciente['id_paciente'] + 1) if last_paciente else 1  # Incrementa ou define como 1

            paciente_dict = {
                'id_paciente': new_id,  # ID inteiro para referência
                'nome': paciente.getNome(),
                'cpf': paciente.getCpf(),
                'sexo': paciente.getSexo(),
                'email': paciente.getEmail(),
                'cep': paciente.getCep(),
                'data_nascimento': str(paciente.getDataNascimento()),  # Convertendo para string
                'telefone': paciente.getTelefone()
            }

            # Insere o paciente no banco de dados
            result = self.collection.insert_one(paciente_dict)

            # Define o ID do paciente inserido no objeto Paciente
            paciente.setIdPaciente(new_id)
            print(f"Paciente criado com sucesso com ID: {new_id}.")
        
        except Exception as e:
            print(f"Erro ao criar paciente: {e}")

    def buscar_paciente(self, id_paciente: int):
        try:
            # Busca o paciente pelo id_paciente
            paciente = self.collection.find_one({"id_paciente": id_paciente})
            if paciente:
                return Paciente(
                    nome=paciente['nome'],
                    cpf=paciente['cpf'],
                    sexo=paciente['sexo'],
                    email=paciente['email'],
                    cep=paciente['cep'],
                    data_nascimento=paciente['data_nascimento'],
                    telefone=paciente['telefone'],
                    id_paciente=paciente['id_paciente']
                )
            else:
                print("Paciente não encontrado.")
                return None

        except Exception as e:
            print(f"Erro ao buscar paciente: {e}")
            return None

    def atualizar_paciente(self, paciente: Paciente):
        try:
            paciente_dict = {
                'nome': paciente.getNome(),
                'cpf': paciente.getCpf(),
                'sexo': paciente.getSexo(),
                'email': paciente.getEmail(),
                'cep': paciente.getCep(),
                'data_nascimento': str(paciente.getDataNascimento()),  # Convertendo para string
                'telefone': paciente.getTelefone()
            }

            # Use id_paciente para buscar e atualizar
            result = self.collection.update_one(
                {'id_paciente': paciente.getIdPaciente()},  # Busca pelo id_paciente (inteiro)
                {'$set': paciente_dict}  # Define os novos valores
            )

            if result.modified_count > 0:
                print("Paciente atualizado com sucesso.")
            else:
                print("Nenhuma alteração foi feita. Verifique os dados.")
        
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")

    def listar_todos_pacientes(self):
        try:
            # Retorna todos os pacientes
            pacientes = self.collection.find()
            lista_pacientes = []
            for paciente in pacientes:
                obj_paciente = Paciente(
                    nome=paciente['nome'],
                    cpf=paciente['cpf'],
                    sexo=paciente['sexo'],
                    email=paciente['email'],
                    cep=paciente['cep'],
                    data_nascimento=paciente['data_nascimento'],
                    telefone=paciente['telefone'],
                    id_paciente=paciente['id_paciente']
                )
                lista_pacientes.append(obj_paciente)
            return lista_pacientes

        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")
            return []

    def deletar_paciente(self, id_paciente: int):
        try:
            # Remove o paciente com base no ID
            result = self.collection.delete_one({'id_paciente': id_paciente})
            if result.deleted_count > 0:
                print("Paciente deletado com sucesso.")
            else:
                print("Nenhum paciente encontrado com o ID fornecido.")
        
        except Exception as e:
            print(f"Erro ao deletar paciente: {e}")
