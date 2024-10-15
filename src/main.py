# src/main.py
import sys
sys.path.append('.')

from src.app.views.consultaView import ConsultaView
from src.app.views.medicoView import MedicoView
from src.app.views.pacienteView import PacienteView

class MainMenu:
    def __init__(self):
        self.consulta_view = ConsultaView()
        self.medico_view = MedicoView()
        self.paciente_view = PacienteView()

    def menu(self):
        while True:
            print("\n--- Sistema de Gestão Clínica ---")
            print("1. Gerenciar Consultas")
            print("2. Gerenciar Médicos")
            print("3. Gerenciar Pacientes")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.consulta_view.menu()
            elif opcao == '2':
                self.medico_view.menu()
            elif opcao == '3':
                self.paciente_view.menu()
            elif opcao == '4':
                print("Saindo do sistema...")
                exit()
            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()
