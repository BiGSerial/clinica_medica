from pymongo import MongoClient
from bson.objectid import ObjectId
from src.app.models.consulta import Consulta

class ConsultaController:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['clinicadb']
        self.collection = self.db['consultas']

    def criar_consulta(self, consulta: Consulta):
        try:
            # Recupera o último ID usado na coleção, ordenando por id_consulta
            last_consulta = self.collection.find_one(sort=[("id_consulta", -1)])
            new_id = (last_consulta['id_consulta'] + 1) if last_consulta else 1  # Incrementa ou define como 1

            consulta_dict = {
                'id_consulta': new_id,  # ID inteiro para referência
                'horario_consulta_realizada': str(consulta.getHorarioConsultaRealizada()),
                'relatorios': consulta.getRelatorios(),
                'status': consulta.getStatus(),
                'data_criacao': str(consulta.getDataCriacao()),
                'id_paciente': int(consulta.getIdPaciente()),
                'id_medico': int(consulta.getIdMedico())
            }

            # Insere a consulta no banco de dados
            result = self.collection.insert_one(consulta_dict)

            # Define o ID da consulta no objeto Consulta
            consulta.setIdConsulta(new_id)
            print(f"Consulta criada com sucesso com ID: {new_id}.")
        
        except Exception as e:
            print(f"Erro ao criar consulta: {e}")

    def buscar_consulta(self, id_consulta: int):
        try:
            # Busca a consulta pelo id_consulta
            consulta = self.collection.find_one({"id_consulta": id_consulta})
            if consulta:
                return Consulta(
                    horario_consulta_realizada=consulta['horario_consulta_realizada'],
                    relatorios=consulta['relatorios'],
                    status=consulta['status'],
                    data_criacao=consulta['data_criacao'],
                    id_paciente=consulta['id_paciente'],
                    id_medico=consulta['id_medico'],
                    id_consulta=consulta['id_consulta']
                )
            else:
                print("Consulta não encontrada.")
                return None

        except Exception as e:
            print(f"Erro ao buscar consulta: {e}")
            return None

    def atualizar_consulta(self, consulta: Consulta):
        try:
            consulta_dict = {
                'horario_consulta_realizada': str(consulta.getHorarioConsultaRealizada()),
                'relatorios': consulta.getRelatorios(),
                'status': consulta.getStatus(),
                'data_criacao': str(consulta.getDataCriacao()),
                'id_paciente': int(consulta.getIdPaciente()),
                'id_medico': int(consulta.getIdMedico())
            }

            # Atualiza a consulta com base no id_consulta
            result = self.collection.update_one(
                {'id_consulta': consulta.getIdConsulta()},  # Busca pelo id_consulta (inteiro)
                {'$set': consulta_dict}  # Define os novos valores
            )

            if result.modified_count > 0:
                print("Consulta atualizada com sucesso.")
            else:
                print("Nenhuma alteração foi feita. Verifique os dados.")
        
        except Exception as e:
            print(f"Erro ao atualizar consulta: {e}")

    def listar_todas_consultas(self):
        try:
            # Agrega informações das coleções relacionadas
            consultas = self.collection.aggregate([
                {
                    '$lookup': {
                        'from': 'medicos',
                        'localField': 'id_medico',
                        'foreignField': 'id_medico',
                        'as': 'medico'
                    }
                },
                {
                    '$lookup': {
                        'from': 'pacientes',
                        'localField': 'id_paciente',
                        'foreignField': 'id_paciente',
                        'as': 'paciente'
                    }
                },
                {
                    '$lookup': {
                        'from': 'especialidades',
                        'localField': 'medico.id_especialidade',
                        'foreignField': 'id_especialidade',
                        'as': 'especialidade'
                    }
                },
                {
                    '$unwind': '$medico'
                },
                {
                    '$unwind': '$paciente'
                },
                {
                    '$unwind': '$especialidade'
                },
                {
                    '$project': {
                        'nome_paciente': '$paciente.nome',
                        'nome_medico': '$medico.nome',
                        'nome_especialidade': '$especialidade.nome_especialidade',
                        'horario_consulta_realizada': 1,
                        'relatorios': 1,
                        'status': 1,
                        'data_criacao': 1,
                        'id_consulta': 1
                    }
                }
            ])
            return list(consultas)
        
        except Exception as e:
            print(f"Erro ao listar consultas: {e}")
            return []

    def deletar_consulta(self, id_consulta: int):
        try:
            # Remove a consulta com base no id_consulta
            result = self.collection.delete_one({'id_consulta': id_consulta})
            if result.deleted_count > 0:
                print("Consulta deletada com sucesso.")
            else:
                print("Nenhuma consulta encontrada com o ID fornecido.")
        
        except Exception as e:
            print(f"Erro ao deletar consulta: {e}")
