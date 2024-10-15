# src/app/views/pacienteView.py

from src.app.controllers.pacienteController import PacienteController
from src.app.models.paciente import Paciente

class PacienteView:
    def __init__(self):
        self.controller = PacienteController()

    def menu(self):
        print("1. Criar Paciente")
        print("2. Buscar Paciente")
        print("3. Atualizar Paciente")
        print("4. Deletar Paciente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            self.criar_paciente()
        elif opcao == '2':
            self.buscar_paciente()
        elif opcao == '3':
            self.atualizar_paciente()
        elif opcao == '4':
            self.deletar_paciente()
        elif opcao == '5':
            exit()
        else:
            print("Opção inválida!")

    def criar_paciente(self):
        nome = input("Digite o nome do paciente: ")
        cpf = input("Digite o CPF: ")
        sexo = input("Digite o sexo (M/F): ")
        email = input("Digite o email: ")
        cep = input("Digite o CEP: ")
        data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
        telefone = input("Digite o telefone: ")

        paciente = Paciente(nome, cpf, sexo, email, cep, data_nascimento, telefone)
        self.controller.criar_paciente(paciente)

    def buscar_paciente(self):
        id_paciente = input("Digite o ID do paciente: ")
        paciente = self.controller.buscar_paciente(id_paciente)
        if paciente:
            print(paciente.toString())

    def atualizar_paciente(self):
        id_paciente = input("Digite o ID do paciente que deseja atualizar: ")
        paciente_existente = self.controller.buscar_paciente(id_paciente)
        if paciente_existente:
            nome = input("Digite o novo nome: ")
            cpf = input("Digite o novo CPF: ")
            sexo = input("Digite o novo sexo (M/F): ")
            email = input("Digite o novo email: ")
            cep = input("Digite o novo CEP: ")
            data_nascimento = input("Digite a nova data de nascimento (YYYY-MM-DD): ")
            telefone = input("Digite o novo telefone: ")

            paciente_atualizado = Paciente(nome, cpf, sexo, email, cep, data_nascimento, telefone)
            paciente_atualizado.setIdPaciente(id_paciente)
            self.controller.atualizar_paciente(paciente_atualizado)

    def deletar_paciente(self):
        id_paciente = input("Digite o ID do paciente a ser deletado: ")
        self.controller.deletar_paciente(id_paciente)

if __name__ == "__main__":
    view = PacienteView()
    while True:
        view.menu()
