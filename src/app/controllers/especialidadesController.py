from pymongo import MongoClient
from bson.objectid import ObjectId
from src.app.models.especialidades import Especialidades

class EspecialidadesController:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['clinicadb']
        self.collection = self.db['especialidades']

    def criar_especialidade(self, especialidade: Especialidades):
        try:
            # Busca o último documento para determinar o maior ID existente
            cursor = self.collection.find().sort("id_especialidade", -1).limit(1)
            last_especialidade = next(cursor, None)
            new_id = (last_especialidade['id_especialidade'] + 1) if last_especialidade else 1

            # Criação do dicionário para inserção no MongoDB
            especialidade_dict = {
                'id_especialidade': new_id,
                'nome_especialidade': especialidade.getNomeEspecialidade()
            }
            
            # Inserção no MongoDB
            self.collection.insert_one(especialidade_dict)

            # Atualiza o ID no objeto da classe Especialidades
            especialidade.setIdEspecialidade(new_id)
            print("Especialidade criada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao criar especialidade: {e}")

    def buscar_especialidade(self, id_especialidade):
        try:
            # Certifique-se de que id_especialidade é do tipo inteiro
            id_especialidade = int(id_especialidade)
            # print(f"Buscando especialidade com id_especialidade: {id_especialidade}")
            
            # Busca especialidade pelo ID
            especialidade = self.collection.find_one({'id_especialidade': id_especialidade})
            
            if especialidade:
              
                # Retorna um objeto Especialidades com os dados encontrados
                return Especialidades(
                    nome_especialidade=especialidade['nome_especialidade'],
                    id_especialidade=especialidade['id_especialidade']
                )
            else:
                print("Especialidade não encontrada.")
                return None
            
        except Exception as e:
            print(f"Erro ao buscar especialidade: {e}")
            return None


    def atualizar_especialidade(self, especialidade: Especialidades):
        try:
            # Certifique-se de que o ID seja do tipo inteiro
            id_especialidade = int(especialidade.getIdEspecialidade())
            print(f"Atualizando especialidade com id_especialidade: {id_especialidade}")
            
            # Atualiza o documento com base no ID
            result = self.collection.update_one(
                {'id_especialidade': id_especialidade},
                {'$set': {'nome_especialidade': especialidade.getNomeEspecialidade()}}
            )
            
            # Verifica se houve uma modificação
            if result.modified_count > 0:
                print("Especialidade atualizada com sucesso.")
            else:
                print("Nenhuma especialidade foi atualizada. Verifique se o ID existe.")
        
        except Exception as e:
            print(f"Erro ao atualizar especialidade: {e}")


    def listar_todas_especialidades(self):
        """
        Retorna uma lista com todas as especialidades cadastradas no banco de dados.
        """
        try:
            # Obtém todos os documentos da coleção
            especialidades = self.collection.find()
            lista_especialidades = []
            
            # Itera sobre os documentos retornados e cria objetos Especialidades
            for esp in especialidades:
                especialidade = Especialidades(
                    nome_especialidade=esp['nome_especialidade'],
                    id_especialidade=esp['id_especialidade']
                )
                lista_especialidades.append(especialidade)
            
            # Retorna a lista de especialidades
            return lista_especialidades
        
        except Exception as e:
            print(f"Erro ao listar especialidades: {e}")
            return []


    def deletar_especialidade(self, id_especialidade):
        try:
            # Certifique-se de que o ID seja do tipo inteiro
            id_especialidade = int(id_especialidade)
            print(f"Deletando especialidade com id_especialidade: {id_especialidade}")
            
            # Remove o documento com o ID correspondente
            result = self.collection.delete_one({'id_especialidade': id_especialidade})
            
            # Verifica se algum documento foi deletado
            if result.deleted_count > 0:
                print("Especialidade deletada com sucesso.")
            else:
                print("Nenhuma especialidade foi deletada. Verifique se o ID existe.")
        
        except Exception as e:
            print(f"Erro ao deletar especialidade: {e}")
