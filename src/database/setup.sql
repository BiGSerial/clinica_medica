-- Criar a tabela ESPECIALIDADES
CREATE TABLE ESPECIALIDADES (
    ID_ESPECIALIDADE NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
    NOME_ESPECIALIDADE VARCHAR2(100) NOT NULL,
    CONSTRAINT ESPECIALIDADES_PK PRIMARY KEY (ID_ESPECIALIDADE)
);

-- Criar a tabela PACIENTES
CREATE TABLE PACIENTES (
    ID_PACIENTE NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
    NOME VARCHAR2(200) NOT NULL,
    CPF VARCHAR2(11) NOT NULL UNIQUE,  -- Ajustado para 11 caracteres
    SEXO CHAR(1) CHECK (SEXO IN ('M', 'F')) NOT NULL,
    EMAIL VARCHAR2(100) NOT NULL UNIQUE,
    CEP VARCHAR2(9) NOT NULL,
    DATA_NASCIMENTO DATE NOT NULL,
    TELEFONE VARCHAR2(13) NOT NULL,
    CONSTRAINT PACIENTES_PK PRIMARY KEY (ID_PACIENTE)
);

-- Criar a tabela MEDICOS
CREATE TABLE MEDICOS (
    ID_MEDICO NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
    NOME VARCHAR2(100) NOT NULL,
    CRM VARCHAR2(9) NOT NULL UNIQUE,
    TELEFONE VARCHAR2(13) NOT NULL,
    EMAIL VARCHAR2(100) NOT NULL UNIQUE,
    CEP VARCHAR2(9) NOT NULL,
    DATA_NASCIMENTO DATE NOT NULL,
    DATA_CONTRATACAO DATE NOT NULL,
    DATA_REGISTRO DATE NOT NULL,
    ID_ESPECIALIDADE NUMBER NOT NULL,
    CONSTRAINT MEDICOS_PK PRIMARY KEY (ID_MEDICO),
    CONSTRAINT MEDICOS_ESPECIALIDADE_FK FOREIGN KEY (ID_ESPECIALIDADE)
        REFERENCES ESPECIALIDADES (ID_ESPECIALIDADE)
);

-- Criar a tabela CONSULTAS
CREATE TABLE CONSULTAS (
    ID_CONSULTA NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
    HORARIO_CONSULTA_REALIZADA DATE NOT NULL,
    RELATORIOS CLOB NOT NULL,
    STATUS VARCHAR2(20) NOT NULL,
    DATA_CRIACAO DATE NOT NULL,
    ID_PACIENTE NUMBER NOT NULL,
    ID_MEDICO NUMBER NOT NULL,
    CONSTRAINT CONSULTAS_PK PRIMARY KEY (ID_CONSULTA),
    CONSTRAINT CONSULTAS_PACIENTE_FK FOREIGN KEY (ID_PACIENTE)
        REFERENCES PACIENTES (ID_PACIENTE),
    CONSTRAINT CONSULTAS_MEDICO_FK FOREIGN KEY (ID_MEDICO)
        REFERENCES MEDICOS (ID_MEDICO)
);
