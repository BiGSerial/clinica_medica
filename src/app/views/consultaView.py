import sys
sys.path.append('.')
from src.app.controllers.consultaController import ConsultaController
from src.app.models.consulta import Consulta
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh

class ConsultaView:
    def __init__(self):
        self.controller = ConsultaController()
       

    def menu(self):
        while True:
            refresh()  # Atualiza a tela
            AppTitle.display_title()
            print("1. Criar Consulta")
            print("2. Buscar Consulta")
            print("3. Atualizar Consulta")
            print("4. Deletar Consulta")
            print("9. Retornar")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.criar_consulta()
            elif opcao == '2':
                self.buscar_consulta()
            elif opcao == '3':
                self.atualizar_consulta()
            elif opcao == '4':
                self.deletar_consulta()
            elif opcao == '9':
                return
            elif opcao == '0':
                exit()
            else:
                print("Opção inválida!")

    def criar_consulta(self):
        refresh()
        AppTitle.display_title()
        horario_consulta = input("Digite o horário da consulta (YYYY-MM-DD HH:MM:SS): ")
        relatorios = input("Digite o relatório: ")
        status = input("Digite o status: ")
        data_criacao = input("Digite a data de criação (YYYY-MM-DD): ")
        id_paciente = input("Digite o ID do paciente: ")
        id_medico = input("Digite o ID do médico: ")

        consulta = Consulta(horario_consulta, relatorios, status, data_criacao, id_paciente, id_medico)
        self.controller.criar_consulta(consulta)

    def buscar_consulta(self):
        refresh()
        AppTitle.display_title()
        id_consulta = input("Digite o ID da consulta: ")
        consulta = self.controller.buscar_consulta(id_consulta)
        if consulta:
            print(consulta.toString())
        input("\nPressione ENTER para voltar ao menu...")

    def atualizar_consulta(self):
        refresh()
        AppTitle.display_title()
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
            consulta_atualizada.setIdConsulta(id_consulta)
            self.controller.atualizar_consulta(consulta_atualizada)
        input("\nPressione ENTER para voltar ao menu...")

    def deletar_consulta(self):
        refresh()
        AppTitle.display_title()
        id_consulta = input("Digite o ID da consulta a ser deletada: ")
        self.controller.deletar_consulta(id_consulta)
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = ConsultaView()
    view.menu()
