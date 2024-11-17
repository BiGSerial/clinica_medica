from datetime import date


class Medico:
    from typing import Optional

    def __init__(self, nome:str, crm:str, telefone:str, email:str, cep:str, data_nascimento:str, data_contratacao:str, data_registro:str, id_especialidade:int, id_medico:Optional[int]=None):
        self.id_medico = id_medico
        self.setNome(nome)
        self.setCrm(crm)
        self.setTelefone(telefone)
        self.setEmail(email)
        self.setCep(cep)
        self.setDataNascimento(data_nascimento)
        self.setDataContratacao(data_contratacao)
        self.setDataRegistro(data_registro)
        self.setIdEspecialidade(id_especialidade)

    def setIdMedico(self, id_medico):
        self.id_medico = id_medico
    
    def getIdMedico(self):
        return self.id_medico

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setCrm(self, crm):
        self.crm = crm
    
    def getCrm(self):
        return self.crm
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def getTelefone(self):
        return self.telefone
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def setCep(self, cep):
        self.cep = cep
    
    def getCep(self):
        return self.cep
    
    def setDataNascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def getDataNascimento(self):
        return self.data_nascimento
    
    def setDataContratacao(self, data_contratacao):
        self.data_contratacao = data_contratacao

    def getDataContratacao(self):
        return self.data_contratacao
    
    def setDataRegistro(self, data_registro):
        self.data_registro = data_registro

    def getDataRegistro(self):
        return self.data_registro
    
    def setIdEspecialidade(self, id_especialidade):
        self.id_especialidade = id_especialidade

    def getIdEspecialidade(self):
        return self.id_especialidade
    
    def toString(self):
        return f'ID Médico: {self.id_medico}, Nome: {self.nome}, CRM: {self.crm}, Telefone: {self.telefone}, Email: {self.email}, CEP: {self.cep}, Data de Nascimento: {self.data_nascimento}, Data de Contratação: {self.data_contratacao}, Data de Registro: {self.data_registro}, ID da Especialidade: {self.id_especialidade}'
