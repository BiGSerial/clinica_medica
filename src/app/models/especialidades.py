class Especialidades:
    id_especialidade = 0

    def __init__(self, nome_especialidade):
        self.setNomeEspecialidade(nome_especialidade)

    def getIdEspecialidade(self):
        return self._id_especialidade

    def setIdEspecialidade(self, id_especialidade):
        self._id_especialidade = id_especialidade

    def getNomeEspecialidade(self):
        return self._nome_especialidade

    def setNomeEspecialidade(self, nome_especialidade):
        self._nome_especialidade = nome_especialidade

    def toString(self):
        return f'ID Especialidade: {self._id_especialidade}, Nome da Especialidade: {self._nome_especialidade}'


