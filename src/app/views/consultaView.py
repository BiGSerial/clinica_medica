import sys

from app.controllers import pacienteController
from app.models import paciente
sys.path.append('.')

from src.app.controllers.pacienteController import PacienteController
from src.app.controllers.medicoController import MedicoController
from app.views.validations import validar_data, validar_texto
from src.app.controllers.consultaController import ConsultaController
from src.app.models.consulta import Consulta
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh

class ConsultaView:
   

    def __init__(self):
        self.controller = ConsultaController()
        self.medicoController = MedicoController()
        self.pacienteController = PacienteController()
       

    def menu(self):
        while True:
            refresh()  # Atualiza a tela
            AppTitle.display_title()
            print("1. Criar Consulta")
            print("2. Buscar Consulta")
            print("3. Atualizar Consulta")
            print("4. Deletar Consulta")
            print("5. Listar Consultas")
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
            elif opcao == '5':
                self.listar_todas_consultas()
            elif opcao == '9':
                return
            elif opcao == '0':
                exit()
            else:
                print("Opção inválida!")

    def criar_consulta(self):
        refresh()
        AppTitle.display_title()
        horario_consulta = validar_data("Digite o horário da consulta (DD/MM/YYYY): ")
        relatorios = validar_texto('Relatorio')
        status = validar_texto("Status")
        data_criacao = validar_data("Digite a data de criação (DD/MM/YYYY): ")

        print("Pacientes Disponíveis:")
        all_pacientes = self.pacienteController.listar_todos_pacientes()

        if not all_pacientes:
            print("Nenhum paciente encontrado.")
            input("\nPressione ENTER para voltar ao menu...")
            return
        
        else:            
            for paciente in all_pacientes:
                print(f"ID: {paciente[0]}, Nome: {paciente[1]}")

        id_paciente = int(input("Digite o ID do paciente: "))

        print("Medicos Disponíveis:")
        all_medicos = self.medicoController.listar_todos_medicos()

        if not all_medicos:
            print("Nenhum medico encontrado.")
            input("\nPressione ENTER para voltar ao menu...")
            return
        
        else:            
            for medico in all_medicos:
                print(f"ID: {medico[0]}, Nome: {medico[2]} - Especialidade: {medico[3]}")

        id_medico = int(input("Digite o ID do médico: "))

        consulta = Consulta(horario_consulta, relatorios, data_criacao, id_paciente, id_medico, status)
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
            horario_consulta = validar_data("Digite o horário da consulta (DD/MM/YYYY): ")
            relatorios = validar_texto('Relatorio')
            status = validar_texto("Status")
            data_criacao = validar_data("Digite a data de criação (DD/MM/YYYY): ")

            print("Pacientes Disponíveis:")
            all_pacientes = self.pacienteController.listar_todos_pacientes()

            if not all_pacientes:
                print("Nenhum paciente encontrado.")
                input("\nPressione ENTER para voltar ao menu...")
                return
            
            else:            
                for paciente in all_pacientes:
                    print(f"ID: {paciente[0]}, Nome: {paciente[1]}")

            id_paciente = int(input("Digite o ID do paciente: "))

            print("Medicos Disponíveis:")
            all_medicos = self.medicoController.listar_todos_medicos()

            if not all_medicos:
                print("Nenhum medico encontrado.")
                input("\nPressione ENTER para voltar ao menu...")
                return
            
            else:            
                for medico in all_medicos:
                    print(f"ID: {medico[0]}, Nome: {medico[2]} - Especialidade: {medico[3]}")

            id_medico = int(input("Digite o ID do médico: "))

            consulta_atualizada = Consulta(horario_consulta, relatorios, data_criacao, id_paciente, id_medico, status)
            consulta_atualizada.setIdConsulta(id_consulta)
            self.controller.atualizar_consulta(consulta_atualizada)
        input("\nPressione ENTER para voltar ao menu...")
    
    def listar_todas_consultas(self):
        refresh()
        AppTitle.display_title()
        consultas = self.controller.listar_todas_consultas()
        if consultas:
            print("\nConsultas disponíveis:")
            for consulta in consultas:
               
                print(f"ID: {consulta[0]}, Horário: {consulta[1]}, Nome Paciente: {consulta[4]}, Nome Médico: {consulta[5]}, Especialidade: {consulta[6]}")
        else:
            print("Nenhuma consulta encontrada.")
        input("\nPressione ENTER para continuar...")

    def deletar_consulta(self):
        refresh()
        AppTitle.display_title()
        id_consulta = input("Digite o ID da consulta a ser deletada: ")
        self.controller.deletar_consulta(id_consulta)
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = ConsultaView()
    view.menu()
