class Consulta:
    def __init__(self, id_consulta, horario_consulta_realizada, relatorios, data_criacao, id_paciente, id_medico):
        self.setIdConsulta(id_consulta)
        self.setHorarioConsultaRealizada(horario_consulta_realizada)
        self.setRelatorios(relatorios)
        self.setDataCriacao(data_criacao)
        self.setIdPaciente(id_paciente)
        self.setIdMedico(id_medico)

    def getIdConsulta(self):
        return self._id_consulta

    def setIdConsulta(self, id_consulta):
        self._id_consulta = id_consulta

    def getHorarioConsultaRealizada(self):
        return self._horario_consulta_realizada

    def setHorarioConsultaRealizada(self, horario_consulta_realizada):
        self._horario_consulta_realizada = horario_consulta_realizada

    def getRelatorios(self):
        return self._relatorios

    def setRelatorios(self, relatorios):
        self._relatorios = relatorios

    def getDataCriacao(self):
        return self._data_criacao

    def setDataCriacao(self, data_criacao):
        self._data_criacao = data_criacao

    def getIdPaciente(self):
        return self._id_paciente

    def setIdPaciente(self, id_paciente):
        self._id_paciente = id_paciente

    def getIdMedico(self):
        return self._id_medico

    def setIdMedico(self, id_medico):
        self._id_medico = id_medico

    def toString(self):
        return f'ID Consulta: {self._id_consulta}, Horário da Consulta Realizada: {self._horario_consulta_realizada}, Relatórios: {self._relatorios}, Data de Criação: {self._data_criacao}, ID Paciente: {self._id_paciente}, ID Médico: {self._id_medico}'

      