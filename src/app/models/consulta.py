class Consulta:
    def __init__(self, horario_consulta_realizada, relatorios, data_criacao, id_paciente, id_medico, status, id_consulta=None):
        self.id_consulta = id_consulta
        self.setHorarioConsultaRealizada(horario_consulta_realizada)
        self.setRelatorios(relatorios)
        self.setDataCriacao(data_criacao)
        self.setIdPaciente(id_paciente)
        self.setIdMedico(id_medico)
        self.setStatus(status)

    def getIdConsulta(self):
        return self.id_consulta

    def setIdConsulta(self, id_consulta):
        self.id_consulta = id_consulta

    def getHorarioConsultaRealizada(self):
        return self.horario_consulta_realizada

    def setHorarioConsultaRealizada(self, horario_consulta_realizada):
        self.horario_consulta_realizada = horario_consulta_realizada

    def getRelatorios(self):
        return self.relatorios

    def setRelatorios(self, relatorios):
        self.relatorios = relatorios

    def getDataCriacao(self):
        return self.data_criacao

    def setDataCriacao(self, data_criacao):
        self.data_criacao = data_criacao

    def getIdPaciente(self):
        return self.id_paciente

    def setIdPaciente(self, id_paciente):
        self.id_paciente = id_paciente

    def getIdMedico(self):
        return self.id_medico

    def setIdMedico(self, id_medico):
        self.id_medico = id_medico

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def toString(self):
        return f'ID Consulta: {self.id_consulta}, Horário da Consulta: {self.horario_consulta_realizada}, Relatórios: {self.relatorios}, Data de Criação: {self.data_criacao}, ID Paciente: {self.id_paciente}, ID Médico: {self.id_medico}, Status: {self.status}'
