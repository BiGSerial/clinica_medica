# src/views/consultaView.py
import sys
sys.path.append('.')

from src.app.controllers.consultaController import ConsultaController
from src.app.models.consulta import Consulta

class ConsultaView:
    def __init__(self):
        self.controller = ConsultaController()

    def menu(self):
        print("1. Criar Consulta")
        print("2. Buscar Consulta")
        print("3. Atualizar Consulta")
        print("4. Deletar Consulta")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            self.criar_consulta()
        elif opcao == '2':
            self.buscar_consulta()
        elif opcao == '3':
            self.atualizar_consulta()
        elif opcao == '4':
            self.deletar_consulta()
        elif opcao == '5':
            exit()
        else:
            print("Opção inválida!")

    def criar_consulta(self):
        horario_consulta = input("Digite o horário da consulta (YYYY-MM-DD HH:MM:SS): ")
        relatorios = input("Digite o relatório: ")
        status = input("Digite o status: ")
        data_criacao = input("Digite a data de criação (YYYY-MM-DD): ")
        id_paciente = input("Digite o ID do paciente: ")
        id_medico = input("Digite o ID do médico: ")

        consulta = Consulta(horario_consulta, relatorios, status, data_criacao, id_paciente, id_medico)
        self.controller.criar_consulta(consulta)

    def buscar_consulta(self):
        id_consulta = input("Digite o ID da consulta: ")
        consulta = self.controller.buscar_consulta(id_consulta)
        if consulta:
            print(consulta.toString())

    def atualizar_consulta(self):
        id_consulta = input("Digite o ID da consulta que deseja atualizar: ")
        consulta_existente = self.controller.buscar_consulta(id_consulta)
        if consulta_existente:
            horario_consulta = input("Digite o novo horário da consulta (YYYY-MM-DD HH:MM:SS): ")
            relatorios = input("Digite o novo relatório: ")
            status = input("Digite o novo status: ")
            data_criacao = input("Digite a nova data de criação (YYYY-MM-DD): ")
            id_paciente = input("Digite o novo ID do paciente: ")
            id_medico = input("Digite o novo ID do médico: ")

            consulta_atualizada = Consulta(horario_consulta, relatorios, status, data_criacao, id_paciente, id_medico)
            self.controller.atualizar_consulta(consulta_atualizada)

    def deletar_consulta(self):
        id_consulta = input("Digite o ID da consulta a ser deletada: ")
        self.controller.deletar_consulta(id_consulta)

if __name__ == "__main__":
    view = ConsultaView()
    while True:
        view.menu()
