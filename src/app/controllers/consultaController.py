# src/app/controllers/consultaController.py
import sys
sys.path.append('.')

from src.database.Database import DatabaseConnection
from src.app.models.consulta import Consulta

class ConsultaController:
    def __init__(self):
        self.db = DatabaseConnection()

    def criar_consulta(self, consulta: Consulta):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''INSERT INTO consultas 
                     (horario_consulta_realizada, relatorios, status, data_criacao, id_paciente, id_medico) 
                     VALUES (:horario_consulta_realizada, :relatorios, :status, :data_criacao, :id_paciente, :id_medico)'''
            
            cursor.execute(sql, {
                'horario_consulta_realizada': consulta.getHorarioConsultaRealizada(),
                'relatorios': consulta.getRelatorios(),
                'status': consulta.getStatus(),
                'data_criacao': consulta.getDataCriacao(),
                'id_paciente': consulta.getIdPaciente(),
                'id_medico': consulta.getIdMedico()
            })

            #Pega o id da consulta criada
            consulta.setIdConsulta(cursor.lastrowid)
            
            if self.db.connection:
                self.db.connection.commit()
                print("Consulta criada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao criar consulta: {e}")
            if self.db.connection:
                self.db.connection.rollback()
        
        finally:
            self.db.disconnect()

    def buscar_consulta(self, id_consulta):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            
            sql = "SELECT * FROM consultas WHERE id_consulta = :id_consulta"
            cursor.execute(sql, {'id_consulta': id_consulta})
            consulta = cursor.fetchone()
            
            if consulta:
                return Consulta(
                    horario_consulta_realizada=consulta[1],
                    relatorios=consulta[2],
                    status=consulta[3],
                    data_criacao=consulta[4],
                    id_paciente=consulta[5],
                    id_medico=consulta[6]
                )
            else:
                print("Consulta não encontrada.")

        
        except Exception as e:
            print(f"Erro ao buscar consulta: {e}")
        
        finally:
            self.db.disconnect()

    def atualizar_consulta(self, consulta: Consulta):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = '''UPDATE consultas SET 
                     horario_consulta_realizada = :horario_consulta_realizada,
                     relatorios = :relatorios, 
                     status = :status,
                     data_criacao = :data_criacao,
                     id_paciente = :id_paciente, 
                     id_medico = :id_medico 
                     WHERE id_consulta = :id_consulta'''
            
            cursor.execute(sql, {
                'id_consulta': consulta.getIdConsulta(),
                'horario_consulta_realizada': consulta.getHorarioConsultaRealizada(),
                'relatorios': consulta.getRelatorios(),
                'status': consulta.getStatus(),
                'data_criacao': consulta.getDataCriacao(),
                'id_paciente': consulta.getIdPaciente(),
                'id_medico': consulta.getIdMedico()
            })
            
            if self.db.connection:
                self.db.connection.commit()
            print("Consulta atualizada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao atualizar consulta: {e}")
        
        finally:
            self.db.disconnect()

    def deletar_consulta(self, id_consulta):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()

            sql = "DELETE FROM consultas WHERE id_consulta = :id_consulta"
            cursor.execute(sql, {'id_consulta': id_consulta})
            
            if self.db.connection:
                self.db.connection.commit()
                print("Consulta deletada com sucesso.")
        
        except Exception as e:
            print(f"Erro ao deletar consulta: {e}")
        
        finally:
            self.db.disconnect()
