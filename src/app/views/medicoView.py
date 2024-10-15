# src/app/views/medicoView.py

from src.app.controllers.medicoController import MedicoController
from src.app.models.medico import Medico

class MedicoView:
    def __init__(self):
        self.controller = MedicoController()

    def menu(self):
        print("1. Criar Médico")
        print("2. Buscar Médico")
        print("3. Atualizar Médico")
        print("4. Deletar Médico")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            self.criar_medico()
        elif opcao == '2':
            self.buscar_medico()
        elif opcao == '3':
            self.atualizar_medico()
        elif opcao == '4':
            self.deletar_medico()
        elif opcao == '5':
            exit()
        else:
            print("Opção inválida!")

    def criar_medico(self):
        nome = input("Digite o nome do médico: ")
        crm = input("Digite o CRM: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        cep = input("Digite o CEP: ")
        data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
        data_contratacao = input("Digite a data de contratação (YYYY-MM-DD): ")
        data_registro = input("Digite a data de registro (YYYY-MM-DD): ")
        id_especialidade = input("Digite o ID da especialidade: ")

        medico = Medico(nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade)
        self.controller.criar_medico(medico)

    def buscar_medico(self):
        id_medico = input("Digite o ID do médico: ")
        medico = self.controller.buscar_medico(id_medico)
        if medico:
            print(medico.toString())

    def atualizar_medico(self):
        id_medico = input("Digite o ID do médico que deseja atualizar: ")
        medico_existente = self.controller.buscar_medico(id_medico)
        if medico_existente:
            nome = input("Digite o novo nome: ")
            crm = input("Digite o novo CRM: ")
            telefone = input("Digite o novo telefone: ")
            email = input("Digite o novo email: ")
            cep = input("Digite o novo CEP: ")
            data_nascimento = input("Digite a nova data de nascimento (YYYY-MM-DD): ")
            data_contratacao = input("Digite a nova data de contratação (YYYY-MM-DD): ")
            data_registro = input("Digite a nova data de registro (YYYY-MM-DD): ")
            id_especialidade = input("Digite o novo ID da especialidade: ")

            medico_atualizado = Medico(nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade)
            medico_atualizado.setIdMedico(id_medico)
            self.controller.atualizar_medico(medico_atualizado)

    def deletar_medico(self):
        id_medico = input("Digite o ID do médico a ser deletado: ")
        self.controller.deletar_medico(id_medico)

if __name__ == "__main__":
    view = MedicoView()
    while True:
        view.menu()
