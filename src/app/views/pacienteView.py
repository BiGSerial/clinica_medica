import sys
sys.path.append('.')
from src.app.controllers.pacienteController import PacienteController
from src.app.models.paciente import Paciente
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh
from src.app.views.validations import validar_inteiro, validar_data, validar_email, validar_texto  # Importando funções de validação

class PacienteView:
    def __init__(self):
        self.controller = PacienteController()

    def menu(self):
        while True:
            refresh()
            AppTitle.display_title()
            print("1. Criar Paciente")
            print("2. Buscar Paciente")
            print("3. Atualizar Paciente")
            print("4. Deletar Paciente")
            print("5. Listar Todos os Pacientes")
            print("9. Retornar")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.criar_paciente()
            elif opcao == '2':
                self.buscar_paciente()
            elif opcao == '3':
                self.atualizar_paciente()
            elif opcao == '4':
                self.deletar_paciente()
            elif opcao == '9':
                return
            elif opcao == '0':
                exit()
            else:
                print("Opção inválida!")

    def criar_paciente(self):
        refresh()
        AppTitle.display_title()
        nome = input("Digite o nome do paciente: ")

        cpf = validar_texto("CPF", 11)
        sexo = validar_texto("Sexo (M/F)", 1, 1)
        email = validar_email("Digite o novo email: ")
        cep = validar_texto("CEP", 8, 8)
        data_nascimento = validar_data("Digite a nova data de nascimento (DD/MM/AAAA): ")
        telefone = validar_texto("Telefone", 9, 11)


        paciente = Paciente(nome, cpf, sexo, data_nascimento, telefone, email, cep)
        self.controller.criar_paciente(paciente)
        input("\nPressione ENTER para voltar ao menu...")

    def buscar_paciente(self):
        refresh()
        AppTitle.display_title()
        id_paciente = validar_inteiro("ID do Paciente")
        if id_paciente is None: return

        paciente = self.controller.buscar_paciente(id_paciente)
        if paciente:
            print(paciente.toString())
        input("\nPressione ENTER para voltar ao menu...")

    def atualizar_paciente(self):
        refresh()
        AppTitle.display_title()
        id_paciente = validar_inteiro("ID do Paciente que deseja atualizar")
        if id_paciente is None: return

        paciente_existente = self.controller.buscar_paciente(id_paciente)
        if paciente_existente:
            nome = input("Digite o novo nome: ")

            cpf = validar_texto("CPF", 11)
            sexo = validar_texto("Sexo (M/F)", 1, 1)
            email = validar_email("Digite o novo email: ")
            cep = validar_texto("CEP", 8, 8)
            data_nascimento = validar_data("Digite a nova data de nascimento (DD/MM/AAAA): ")
            telefone = validar_texto("Telefone", 9, 11)

            paciente_atualizado = Paciente(nome, cpf, sexo, data_nascimento, telefone, email, cep)
            paciente_atualizado.setIdPaciente(id_paciente)
            self.controller.atualizar_paciente(paciente_atualizado)

        input("\nPressione ENTER para voltar ao menu...")

    def deletar_paciente(self):
        refresh()
        AppTitle.display_title()
        print('')
        pacientes = self.controller.listar_todos_pacientes()
        if pacientes:
            for paciente in pacientes:
               print(f"ID: {paciente[0]}, Nome: {paciente[1]}, CPF: {paciente[2]}, SEXO: {paciente[3]}")

        print('')
        id_paciente = validar_inteiro("ID do Paciente a ser deletado")       

        if id_paciente is None: return

        self.controller.deletar_paciente(id_paciente)
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = PacienteView()
    view.menu()
