from pydoc import doc
import sys
sys.path.append('.')
from src.app.controllers.medicoController import MedicoController
from src.app.models.medico import Medico
from src.app.views.appTitle import AppTitle, SplashScreen
from src.app.views.utils import refresh
from src.app.views.validations import validar_inteiro, validar_data, validar_email, validar_texto

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
                print(f"ID: {medico.getIdMedico()}, CRM: {medico.getCrm()}, Nome: {medico.getNome()}, Especialidade: {medico.getIdEspecialidade()}")
        else:
            print("Nenhum médico encontrado.")
        input("\nPressione ENTER para continuar...")

    def criar_medico(self):
        refresh()
        AppTitle.display_title()
        nome = input("Digite o nome do médico: ")

        crm = validar_texto("CRM", 9)
        telefone = validar_texto("Telefone", 11)
        email = validar_email("Digite o email: ")
        cep = validar_texto("CEP", 8)
        data_nascimento = validar_data("Digite a data de nascimento (DD/MM/AAAA): ")
        data_contratacao = validar_data("Digite a data de contratação (DD/MM/AAAA): ")
        data_registro = validar_data("Digite a data de registro (DD/MM/AAAA): ")
        id_especialidade = validar_inteiro("ID da Especialidade")

        # Debugging: Dump the variables to see their contents
        print(f"Nome: {nome}")
        print(f"CRM: {crm}")
        print(f"Telefone: {telefone}")
        print(f"Email: {email}")
        print(f"CEP: {cep}")
        print(f"Data de Nascimento: {data_nascimento}")
        print(f"Data de Contratação: {data_contratacao}")
        print(f"Data de Registro: {data_registro}")
        print(f"ID da Especialidade: {id_especialidade}")

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
            id_medico = input("Digite o ID do médico: ")
            if id_medico is None: return

            medico = self.controller.buscar_medico(int(id_medico))
            
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

        id_medico = validar_inteiro("ID do médico que deseja atualizar")
       

        medico_existente = self.controller.buscar_medico(id_medico)
        if medico_existente:
            nome = input("Digite o novo nome: ")

            crm = validar_texto("CRM", 9)
            telefone = validar_texto("Telefone", 11)
            email = validar_email("Digite o novo email: ")
            cep = validar_texto("CEP", 8)
            data_nascimento = validar_data("Digite a nova data de nascimento (DD/MM/AAAA): ")
            data_contratacao = validar_data("Digite a nova data de contratação (DD/MM/AAAA): ")
            data_registro = validar_data("Digite a nova data de registro (DD/MM/AAAA): ")
            id_especialidade = validar_inteiro("ID da Especialidade")

            medico_atualizado = Medico(nome, crm, telefone, email, cep, data_nascimento, data_contratacao, data_registro, id_especialidade)
            medico_atualizado.setIdMedico(id_medico)
            self.controller.atualizar_medico(medico_atualizado)

        input("\nPressione ENTER para voltar ao menu...")

    def listar_todos_pacientes(self):
        refresh()
        AppTitle.display_title()
        print("\nLista de Todos os Pacientes:\n")
        
        # Obtém todos os pacientes do controller
        pacientes = self.controller.listar_todos_pacientes()
        
        if pacientes:
            for paciente in pacientes:
                print(f"ID: {paciente.getIdPaciente()}, Nome: {paciente.getNome()}, CPF: {paciente.getCpf()}, Sexo: {paciente.getSexo()}, Data de Nascimento: {paciente.getDataNascimento()}, Telefone: {paciente.getTelefone()}, Email: {paciente.getEmail()}, CEP: {paciente.getCep()}")
        else:
            print("Nenhum paciente encontrado.")
        
        input("\nPressione ENTER para voltar ao menu...")



    def deletar_medico(self):
        refresh()
        AppTitle.display_title()
        id_medico = input("Digite o ID do médico a ser deletado: ")
        if id_medico is None: return

        self.controller.deletar_medico(int(id_medico))
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    view = MedicoView()
    view.menu()
