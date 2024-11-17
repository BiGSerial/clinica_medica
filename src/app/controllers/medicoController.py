from pymongo import MongoClient
from bson.objectid import ObjectId
from src.app.models.medico import Medico

class MedicoController:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['clinicadb']
        self.collection = self.db['medicos']
        self.especialidades_collection = self.db['especialidades']

    def criar_medico(self, medico: Medico):
        try:
            # Recupera o último ID usado na coleção, ordenando por id_medico
            last_medico = self.collection.find_one(sort=[("id_medico", -1)])
            new_id = (last_medico['id_medico'] + 1) if last_medico else 1  # Incrementa ou define como 1

            medico_dict = {
                'id_medico': new_id,  # ID inteiro para referência
                'nome': medico.getNome(),
                'crm': medico.getCrm(),
                'telefone': medico.getTelefone(),
                'email': medico.getEmail(),
                'cep': medico.getCep(),
                'data_nascimento': str(medico.getDataNascimento()),  # Convertendo para string
                'data_contratacao': str(medico.getDataContratacao()),  # Convertendo para string
                'data_registro': str(medico.getDataRegistro()),  # Convertendo para string
                'id_especialidade': medico.getIdEspecialidade()
            }

            # Insere o médico no banco de dados
            result = self.collection.insert_one(medico_dict)

            # Define o ID do médico inserido no objeto Medico
            medico.setIdMedico(new_id)
            print(f"Médico criado com sucesso com ID: {new_id}.")
        
        except Exception as e:
            print(f"Erro ao criar médico: {e}")


    def buscar_medico(self, id_medico: int):
        try:
            # Busca o médico pelo id_medico
            medico = self.collection.find_one({"id_medico": id_medico})
            if medico:
                # Busca o nome da especialidade correspondente
                especialidade = self.especialidades_collection.find_one({"id_especialidade": medico['id_especialidade']})
                nome_especialidade = especialidade['nome_especialidade'] if especialidade else "Desconhecida"

                return (
                    medico['id_medico'],
                    medico['crm'],
                    medico['nome'],
                    nome_especialidade
                )
            else:
                print("Médico não encontrado.")
                return None

        except Exception as e:
            print(f"Erro ao buscar médico: {e}")
            return None


    def buscar_medico_por_nome(self, nome_parcial: str):
        try:
            # Busca médicos cujo nome contenha a string parcial (case insensitive)
            query = {'nome': {'$regex': nome_parcial, '$options': 'i'}}
            medicos = self.collection.find(query)

            resultado = []
            for medico in medicos:
                # Busca o nome da especialidade correspondente
                especialidade = self.especialidades_collection.find_one({'id_especialidade': medico['id_especialidade']})
                nome_especialidade = especialidade['nome_especialidade'] if especialidade else "Desconhecida"

                resultado.append((
                    medico['id_medico'],
                    medico['crm'],
                    medico['nome'],
                    nome_especialidade
                ))

            return resultado

        except Exception as e:
            print(f"Erro ao buscar médicos por nome parcial: {e}")
            return []

    def atualizar_medico(self, medico: Medico):
        try:
            medico_dict = {
                'nome': medico.getNome(),
                'crm': medico.getCrm(),
                'telefone': medico.getTelefone(),
                'email': medico.getEmail(),
                'cep': medico.getCep(),
                'data_nascimento': str(medico.getDataNascimento()),
                'data_contratacao': str(medico.getDataContratacao()),
                'data_registro': str(medico.getDataRegistro()),
                'id_especialidade': medico.getIdEspecialidade()
            }

            # Use id_medico para buscar e atualizar
            result = self.collection.update_one(
                {'id_medico': medico.getIdMedico()},  # Busca pelo id_medico (inteiro)
                {'$set': medico_dict}  # Define os novos valores
            )

            if result.modified_count > 0:
                print("Médico atualizado com sucesso.")
            else:
                print("Nenhuma alteração foi feita. Verifique os dados.")
        
        except Exception as e:
            print(f"Erro ao atualizar médico: {e}")


    def listar_todos_medicos(self):
        try:
            # Retorna todos os médicos
            medicos = self.collection.find()
            lista_medicos = []
            for medico in medicos:
                obj_medico = Medico(
                    nome=medico['nome'],
                    crm=medico['crm'],
                    telefone=medico['telefone'],
                    email=medico['email'],
                    cep=medico['cep'],
                    data_nascimento=medico['data_nascimento'],  # Já será uma string
                    data_contratacao=medico['data_contratacao'],  # Já será uma string
                    data_registro=medico['data_registro'],  # Já será uma string
                    id_especialidade=medico['id_especialidade'],
                    id_medico=str(medico['id_medico'])
                )
                lista_medicos.append(obj_medico)
            return lista_medicos
        
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")
            return []

    def deletar_medico(self, id_medico: int):
        try:
            # Remove o médico com base no ID
            result = self.collection.delete_one({'id_medico': id_medico})
            if result.deleted_count > 0:
                print("Médico deletado com sucesso.")
            else:
                print("Nenhum médico encontrado com o ID fornecido.")
        
        except Exception as e:
            print(f"Erro ao deletar médico: {e}")
