import sys
sys.path.append('.')
from src.app.controllers.pacienteController import PacienteController
from src.app.models.paciente import Paciente
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh
from src.app.views.validations import validar_inteiro, validar_data, validar_email  # Importando funções de validação

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

        cpf = validar_inteiro(input("Digite o CPF (somente números): "), "CPF")
        if cpf is None: return

        sexo = input("Digite o sexo (M/F): ").upper()
        if sexo not in ['M', 'F']:
            print("Sexo inválido. Insira 'M' para masculino ou 'F' para feminino.")
            return

        email = validar_email(input("Digite o email: "))
        if email is None: return

        cep = validar_inteiro(input("Digite o CEP (somente números): "), "CEP")
        if cep is None: return

        data_nascimento = validar_data(input("Digite a data de nascimento (DD/MM/AAAA): "))
        if data_nascimento is None: return

        telefone = validar_inteiro(input("Digite o telefone (somente números): "), "Telefone")
        if telefone is None: return

        paciente = Paciente(nome, cpf, sexo, data_nascimento, telefone ,email, cep)
        self.controller.criar_paciente(paciente)
        input("\nPressione ENTER para voltar ao menu...")

    def buscar_paciente(self):
        refresh()
        AppTitle.display_title()
        id_paciente = validar_inteiro(input("Digite o ID do paciente: "), "ID do Paciente")
        if id_paciente is None: return

        paciente = self.controller.buscar_paciente(id_paciente)
        if paciente:
            print(paciente.toString())
        input("\nPressione ENTER para voltar ao menu...")

    def atualizar_paciente(self):
        refresh()
        AppTitle.display_title()
        id_paciente = validar_inteiro(input("Digite o ID do paciente que deseja atualizar: "), "ID do Paciente")
        if id_paciente is None: return

        paciente_existente = self.controller.buscar_paciente(id_paciente)
        if paciente_existente:
            nome = input("Digite o novo nome: ")

            cpf = validar_inteiro(input("Digite o novo CPF (somente números): "), "CPF")
            if cpf is None: return

            sexo = input("Digite o novo sexo (M/F): ").upper()
            if sexo not in ['M', 'F']:
                print("Sexo inválido. Insira 'M' para masculino ou 'F' para feminino.")
                return

            email = validar_email(input("Digite o novo email: "))
            if email is None: return

            cep = validar_inteiro(input("Digite o novo CEP (somente números): "), "CEP")
            if cep is None: return

            data_nascimento = validar_data(input("Digite a nova data de nascimento (DD/MM/AAAA): "))
            if data_nascimento is None: return

            telefone = validar_inteiro(input("Digite o novo telefone (somente números): "), "Telefone")
            if telefone is None: return

                                                   
            paciente_atualizado = Paciente(nome, cpf, sexo, data_nascimento, telefone ,email, cep)
            paciente_atualizado.setIdPaciente(id_paciente)
            self.controller.atualizar_paciente(paciente_atualizado)
        input("\nPressione ENTER para voltar ao menu...")

    def deletar_paciente(self):
        refresh()
        AppTitle.display_title()
        id_paciente = validar_inteiro(input("Digite o ID do paciente a ser deletado: "), "ID do Paciente")
        if id_paciente is None: return

        self.controller.deletar_paciente(id_paciente)
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = PacienteView()
    view.menu()
