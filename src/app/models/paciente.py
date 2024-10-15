# src/app/models/paciente.pyds
class Paciente:

    id_paciente:int = 0

    def __init__(self, nome, cpf, sexo, data_nascimento, telefone, email, cep):        
        
        self.setNome(nome)
        self.setCpf(cpf)
        self.setSexo(sexo)
        self.setDataNascimento(data_nascimento)
        self.setTelefone(telefone)
        self.setEmail(email)
        self.setCep(cep)
             

    def setIdPaciente(self, id_paciente):
        self.id_paciente = id_paciente
    
    def getIdPaciente(self):
        return self.id_paciente

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setCpf(self, cpf):
        self.cpf = cpf
    
    def getCpf(self):
        return self.cpf

    def setSexo(self, sexo):
        self.sexo = sexo
    
    def getSexo(self):
        return self.sexo
    
    def setDataNascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
    
    def getDataNascimento(self):
        return self.data_nascimento

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
    

    def toString(self):
        return f'ID: {self.id_paciente}, Nome: {self.nome}, CPF: {self.cpf}, Sexo: {self.sexo}, Data de Nascimento: {self.data_nascimento}, Telefone: {self.telefone}, Email: {self.email}, CEP: {self.cep}'