import sys
sys.path.append('.')
from src.app.controllers.medicoController import MedicoController
from src.app.models.medico import Medico
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh
from src.app.views.validations import validar_inteiro, validar_data, validar_email

class MedicoView:
    def __init__(self):
        self.controller = MedicoController()

    def menu(self):
        while True:
            refresh()
            AppTitle.display_title()
            print("1. Criar Médico")
            print("2. Buscar Médico")
            print("3. Atualizar Médico")
            print("4. Deletar Médico")
            print("9. Retornar")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.criar_medico()
            elif opcao == '2':
                self.buscar_medico()
            elif opcao == '3':
                self.atualizar_medico()
            elif opcao == '4':
                self.deletar_medico()
            elif opcao == '9':
                return
            elif opcao == '0':
                exit()
            else:
                print("Opção inválida!")

    def listar_todos_medicos(self):
        """
        Lista todos os médicos com ID, CRM, nome e especialidade.
        """
        medicos = self.controller.listar_todos_medicos()
        if medicos:
            print("\nMédicos disponíveis:")
            for medico in medicos:
                print(f"ID: {medico[0]}, CRM: {medico[1]}, Nome: {medico[2]}, Especialidade: {medico[3]}")
        else:
            print("Nenhum médico encontrado.")
        input("\nPressione ENTER para continuar...")

    def criar_medico(self):
        refresh()
        AppTitle.display_title()
        nome = input("Digite o nome do médico: ")
        
        crm = validar_inteiro(input("Digite o CRM (somente números): "), "CRM", 9)
        if crm is None: return

        telefone = validar_inteiro(input("Digite o telefone (somente números): "), "Telefone", 11)
        if telefone is None: return

        email = validar_email(input("Digite o email: "))
        if email is None: return

        cep = validar_inteiro(input("Digite o CEP (somente números): "), "CEP", 8)
        if cep is None: return

        data_nascimento = validar_data(input("Digite a data de nascimento (DD/MM/AAAA): "))
        if data_nascimento is None: return

        data_contratacao = validar_data(input("Digite a data de contratação (DD/MM/AAAA): "))
        if data_contratacao is None: return

        data_registro = validar_data(input("Digite a data de registro (DD/MM/AAAA): "))
        if data_registro is None: return

        id_especialidade = validar_inteiro(input("Digite o ID da especialidade: "), "ID da Especialidade")
        if id_especialidade is None: return

        medico = Medico(nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade)
        self.controller.criar_medico(medico)
        input("\nPressione ENTER para voltar ao menu...")

    def buscar_medico(self):
        refresh()
        AppTitle.display_title()
        print("1. Buscar por ID")
        print("2. Buscar por nome parcial")
        opcao = input("Escolha uma opção de busca: ")

        if opcao == '1':
            # Buscar por ID
            id_medico = validar_inteiro(input("Digite o ID do médico: "), "ID do Médico")
            if id_medico is None: return

            medico = self.controller.buscar_medico(id_medico)
            if medico:
                print(f"ID: {medico[0]}, CRM: {medico[1]}, Nome: {medico[2]}, Especialidade: {medico[3]}")
            else:
                print("Médico não encontrado.")
        elif opcao == '2':
            # Buscar por nome parcial
            nome_parcial = input("Digite parte do nome do médico: ")
            medicos = self.controller.buscar_medico_por_nome(nome_parcial)
            if medicos:
                print("\nMédicos encontrados:")
                for medico in medicos:
                    print(f"ID: {medico[0]}, CRM: {medico[1]}, Nome: {medico[2]}, Especialidade: {medico[3]}")
            else:
                print("Nenhum médico encontrado com esse nome.")
        else:
            print("Opção inválida!")

        input("\nPressione ENTER para voltar ao menu...")

    def atualizar_medico(self):
        refresh()
        AppTitle.display_title()

        # Exibe todos os médicos com ID, CRM, nome e especialidade
        self.listar_todos_medicos()

        id_medico = validar_inteiro(input("Digite o ID do médico que deseja atualizar: "), "ID do Médico")
        if id_medico is None: return

        medico_existente = self.controller.buscar_medico(id_medico)
        if medico_existente:
            nome = input("Digite o novo nome: ")

            crm = validar_inteiro(input("Digite o novo CRM (somente números): "), "CRM", 9)
            if crm is None: return

            telefone = validar_inteiro(input("Digite o novo telefone (somente números): "), "Telefone", 11)
            if telefone is None: return

            email = validar_email(input("Digite o novo email: "))
            if email is None: return

            cep = validar_inteiro(input("Digite o novo CEP (somente números): "), "CEP", 8)
            if cep is None: return

            data_nascimento = validar_data(input("Digite a nova data de nascimento (DD/MM/AAAA): "))
            if data_nascimento is None: return

            data_contratacao = validar_data(input("Digite a nova data de contratação (DD/MM/AAAA): "))
            if data_contratacao is None: return

            data_registro = validar_data(input("Digite a nova data de registro (DD/MM/AAAA): "))
            if data_registro is None: return

            id_especialidade = validar_inteiro(input("Digite o novo ID da especialidade: "), "ID da Especialidade")
            if id_especialidade is None: return

            medico_atualizado = Medico(nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade)
            medico_atualizado.setIdMedico(id_medico)
            self.controller.atualizar_medico(medico_atualizado)
        input("\nPressione ENTER para voltar ao menu...")

    def deletar_medico(self):
        refresh()
        AppTitle.display_title()
        id_medico = validar_inteiro(input("Digite o ID do médico a ser deletado: "), "ID do Médico")
        if id_medico is None: return

        self.controller.deletar_medico(id_medico)
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = MedicoView()
    view.menu()
