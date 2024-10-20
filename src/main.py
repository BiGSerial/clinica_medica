from re import S
import sys
sys.path.append('.')

from src.app.views.consultaView import ConsultaView
from src.app.views.medicoView import MedicoView
from src.app.views.pacienteView import PacienteView
from src.app.views.especialidadesView import EspecialidadesView
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh

class MainMenu:
    def __init__(self):
        self.consulta_view = ConsultaView()
        self.medico_view = MedicoView()
        self.paciente_view = PacienteView()
        self.especialidade_view = EspecialidadesView()

    def menu(self):
        while True:
            refresh()  # Limpa a tela
            AppTitle.display_title()  # Exibe o título do aplicativo
            print("\n--- Menu Principal ---")
            print("1. Gerenciar Consultas")
            print("2. Gerenciar Médicos")
            print("3. Gerenciar Pacientes")
            print("4. Gerenciar Especialidades")
            print("0. Sair")
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.consulta_view.menu()
            elif opcao == '2':
                self.medico_view.menu()
            elif opcao == '3':
                self.paciente_view.menu()
            elif opcao == '4':
                self.especialidade_view.menu()
            elif opcao == '0':
                print("Saindo do sistema...")
                exit()
            else:
                print("Opção inválida! Tente novamente.")
                input("\nPressione ENTER para continuar...")  # Espera antes de atualizar o menu

if __name__ == "__main__":
    refresh()
    SplashScreen.show()  # Exibe a splash screen no início
    main_menu = MainMenu()
    main_menu.menu()
