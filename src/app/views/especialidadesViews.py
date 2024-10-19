# src/app/views/especialidadeView.py
import sys
sys.path.append('.')

from src.app.controllers.especialidadesController import EspecialidadesController
from src.app.models.especialidades import Especialidades

class EspecialidadesView:
    def __init__(self):
        self.controller = EspecialidadeController()

    def menu(self):
        print("1. Criar Especialidade")
        print("2. Buscar Especialidade")
        print("3. Atualizar Especialidade")
        print("4. Deletar Especialidade")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            self.criar_especialidade()
        elif opcao == '2':
            self.buscar_especialidade()
        elif opcao == '3':
            self.atualizar_especialidade()
        elif opcao == '4':
            self.deletar_especialidade()
        elif opcao == '5':
            exit()
        else:
            print("Opção inválida!")

    def criar_especialidade(self):
        nome_especialidade = input("Digite o nome da especialidade: ")

        especialidades = Especialidades(nome_especialidade)
        self.controller.criar_especialidade(especialidades)

    def buscar_especialidade(self):
        id_especialidade = input("Digite o ID da especialidade: ")
        especialidade = self.controller.buscar_especialidade(id_especialidade)
        if especialidade:
            print(especialidade.toString())

    def atualizar_especialidade(self):
        id_especialidade = input("Digite o ID da especialidade que deseja atualizar: ")
        especialidade_existente = self.controller.buscar_especialidade(id_especialidade)
        if especialidade_existente:
            nome_especialidade = input("Digite o novo nome da especialidade: ")

            especialidade_atualizada = Especialidades(id_especialidade, nome_especialidade)
            self.controller.atualizar_especialidade(especialidade_atualizada)

    def deletar_especialidade(self):
        id_especialidade = input("Digite o ID da especialidade a ser deletada: ")
        self.controller.deletar_especialidade(id_especialidade)

if __name__ == "__main__":
    view = EspecialidadesView()
    while True:
        view.menu()
