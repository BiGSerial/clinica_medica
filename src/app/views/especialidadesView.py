from re import A
import sys
sys.path.append('.')
from src.app.controllers.especialidadesController import EspecialidadesController
from src.app.models.especialidades import Especialidades
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh

class EspecialidadesView:
    def __init__(self):
        self.controller = EspecialidadesController()

    def menu(self):
        while True:
            refresh()
            AppTitle.display_title()
            print("1. Criar Especialidade")
            print("2. Buscar Especialidade")
            print("3. Atualizar Especialidade")
            print("4. Deletar Especialidade")
            print("9. Retornar")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.criar_especialidade()
            elif opcao == '2':
                self.buscar_especialidade()
            elif opcao == '3':
                self.atualizar_especialidade()
            elif opcao == '4':
                self.deletar_especialidade()
            elif opcao == '9':
                return
            elif opcao == '0':
                exit()
            else:
                print("Opção inválida!")

    def criar_especialidade(self):
        refresh()
        AppTitle.display_title()
        nome_especialidade = input("Digite o nome da especialidade: ")
        especialidade = Especialidades(nome_especialidade)
        self.controller.criar_especialidade(especialidade)
        input("\nPressione ENTER para voltar ao menu...")

    def buscar_especialidade(self):
        refresh()
        AppTitle.display_title()
        id_especialidade = input("Digite o ID da especialidade: ")
        especialidade = self.controller.buscar_especialidade(id_especialidade)
        if especialidade:
            print(especialidade.toString())
        input("\nPressione ENTER para voltar ao menu...")

    def listar_especialidades(self):
        """
        Exibe todas as especialidades disponíveis no sistema.
        """
        refresh()
        AppTitle.display_title()
        especialidades = self.controller.listar_todas_especialidades()
        if especialidades:
            print("\nEspecialidades disponíveis:")
            for esp in especialidades:
                print(f"ID: {esp.getIdEspecialidade()}, Nome: {esp.getNomeEspecialidade()}")
        else:
            print("Nenhuma especialidade encontrada.")
        input("\nPressione ENTER para continuar...")

    def atualizar_especialidade(self):
        """
        Exibe as especialidades disponíveis e permite ao usuário selecionar uma para atualizar.
        """
        especialidades = self.controller.listar_todas_especialidades()
        if especialidades:
            refresh()
            AppTitle.display_title()
            print("\nEspecialidades disponíveis para atualização:")
            for esp in especialidades:
                print(f"ID: {esp.getIdEspecialidade()}, Nome: {esp.getNomeEspecialidade()}")

            id_especialidade = input("\nDigite o ID da especialidade que deseja atualizar: ")
            especialidade_existente = self.controller.buscar_especialidade(id_especialidade)
            if especialidade_existente:
                nome_especialidade = input("Digite o novo nome da especialidade: ")
                especialidade_atualizada = Especialidades(nome_especialidade)
                especialidade_atualizada.setIdEspecialidade(id_especialidade)
                self.controller.atualizar_especialidade(especialidade_atualizada)
                print("Especialidade atualizada com sucesso!")
            else:
                print("Especialidade não encontrada!")
        else:
            print("Nenhuma especialidade disponível para atualização.")
        input("\nPressione ENTER para voltar ao menu...")

    def deletar_especialidade(self):
        """
        Exibe as especialidades disponíveis e permite ao usuário selecionar uma para deletar.
        """
        especialidades = self.controller.listar_todas_especialidades()
        if especialidades:
            print("\nEspecialidades disponíveis para exclusão:")
            for esp in especialidades:
                print(f"ID: {esp.getIdEspecialidade()}, Nome: {esp.getNomeEspecialidade()}")

            id_especialidade = input("\nDigite o ID da especialidade a ser deletada: ")
            especialidade_existente = self.controller.buscar_especialidade(id_especialidade)
            if especialidade_existente:
                confirmacao = input(f"Tem certeza que deseja deletar a especialidade '{especialidade_existente.getNomeEspecialidade()}'? (S/N): ").upper()
                if confirmacao == 'S':
                    self.controller.deletar_especialidade(id_especialidade)
                    print("Especialidade deletada com sucesso!")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Especialidade não encontrada!")
        else:
            print("Nenhuma especialidade disponível para exclusão.")
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = EspecialidadesView()
    view.menu()
