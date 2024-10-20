class Especialidades:
    def __init__(self, nome_especialidade, id_especialidade=None):
        self.id_especialidade = id_especialidade
        self.setNomeEspecialidade(nome_especialidade)

    def getIdEspecialidade(self):
        return self.id_especialidade

    def setIdEspecialidade(self, id_especialidade):
        self.id_especialidade = id_especialidade

    def getNomeEspecialidade(self):
        return self.nome_especialidade

    def setNomeEspecialidade(self, nome_especialidade):
        self.nome_especialidade = nome_especialidade

    def toString(self):
        return f'ID Especialidade: {self.id_especialidade}, Nome da Especialidade: {self.nome_especialidade}'
