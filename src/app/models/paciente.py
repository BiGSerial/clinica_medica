class Paciente:

    def __init__(self, nome, cpf, sexo, data_nascimento, telefone, email):        
        self.setNome(nome)
        self.setCpf(cpf)
        self.setSexo(sexo)
        self.setDataNascimento(data_nascimento)
        self.setTelefone(telefone)
        self.setEmail(email)
             

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
    

    def toString(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Sexo: {self.sexo}, Data de Nascimento: {self.data_nascimento}, Telefone: {self.telefone}, Email: {self.email}'