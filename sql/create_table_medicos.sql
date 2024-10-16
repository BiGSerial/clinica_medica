/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.PACIENTES DROP CONSTRAINT PACIENTES_PK;
ALTER TABLE LABDATABASE.MEDICOS DROP CONSTRAINT MEDICOS_PK;
ALTER TABLE LABDATABASE.ESPECIALIDADES DROP CONSTRAINT ESPECIALIDADES_PK;
ALTER TABLE LABDATABASE.CONSULTAS DROP CONSTRAINT CONSULTAS_PK;
ALTER TABLE LABDATABASE.CONSULTAS DROP CONSTRAINT CONSULTAS_PACIENTE_FK;
ALTER TABLE LABDATABASE.CONSULTAS DROP CONSTRAINT CONSULTAS_MEDICO_FK;

/*Apaga as tabelas*/  --- #
DROP TABLE LABDATABASE.MEDICOS;
DROP TABLE LABDATABASE.PACIENTES;
DROP TABLE LABDATABASE.CONSULTAS;
DROP TABLE LABDATABASE.ESPECIALIDADES;

/*Apaga as sequences*/
DROP SEQUENCE LABDATABASE.PACIENTES_ID_PACIENTE_SEQ;
DROP SEQUENCE LABDATABASE.MEDICOS_ID_MEDICO_SEQ;
DROP SEQUENCE LABDATABASE.CONSULTAS_ID_CONSULTA_SEQ;
DROP SEQUENCE LABDATABASE.ESPECIALIDADES_ID_ESPECIALIDADE_SEQ;

/*Cria as tabelas*/  --- #
CREATE TABLE LABDATABASE.PACIENTES (
    ID_PACIENTE NUMERIC NOT NULL, 
    NOME VARCHAR(200) NOT NULL,
    CPF VARCHAR(13) NOT NULL,
    SEXO VARCHAR(1) NOT NULL, 
    EMAIL VARCHAR(100) NOT NULL, 
    CEP VARCHAR(9) NOT NULL,
    DATA_NASCIMENTO DATE NOT NULL,
    TELEFONE VARCHAR(13) NOT NULL,
    CONSTRAINT PACIENTES_PK PRIMARY KEY (ID_PACIENTE)
);

CREATE TABLE LABDATABASE.MEDICOS (
    ID_MEDICO NUMERIC NOT NULL, 
    NOME VARCHAR(100) NOT NULL,
    CRM VARCHAR(9) NOT NULL,
    TELEFONE VARCHAR(13) NOT NULL,
    EMAIL VARCHAR(100) NOT NULL,
    CEP VARCHAR(9) NOT NULL, 
    DATA_NASCIMENTO DATE NOT NULL,
    DATA_CONTRATACAO DATE NOT NULL, 
    DATA_REGISTRO DATE NOT NULL,
    ID_ESPECIALIDADE NUMERIC NOT NULL,
    CONSTRAINT MEDICOS_PK PRIMARY KEY (ID_MEDICO)
);

CREATE TABLE LABDATABASE.ESPECIALIDADES (
    ID_ESPECIALIDADE NUMERIC NOT NULL,
    NOME_ESPECIALIDADE VARCHAR(100) NOT NULL,
    CONSTRAINT ESPECIALIDADES_PK PRIMARY KEY (ID_ESPECIALIDADE)
);

CREATE TABLE CONSULTAS (
    ID_CONSULTA NUMERIC NOT NULL, 
    HORARIO_CONSULTA_REALIZADA DATE NOT NULL,
    RELATORIOS CLOB NOT NULL,
    STATUS VARCHAR(20) NOT NULL, 
    DATA_CRIACAO DATE NOT NULL,
    ID_PACIENTE NUMERIC NOT NULL,
    ID_MEDICO NUMERIC NOT NULL,
    CONSTRAINT CONSULTAS_PK PRIMARY KEY (ID_CONSULTA),
    CONSTRAINT CONSULTAS_PACIENTE_FK FOREIGN KEY (ID_PACIENTE) REFERENCES PACIENTES (ID_PACIENTE),
    CONSTRAINT CONSULTAS_MEDICO_FK FOREIGN KEY (ID_MEDICO) REFERENCES MEDICOS (ID_MEDICO)
);


/*Cria as sequences*/
CREATE SEQUENCE LABDATABASE.PACIENTES_ID_PACIENTE_SEQ;
CREATE SEQUENCE LABDATABASE.MEDICOS_ID_MEDICO_SEQ;
CREATE SEQUENCE LABDATABASE.CONSULTAS_ID_CONSULTA_SEQ;
CREATE SEQUENCE LABDATABASE.ESPECIALIDADES_ID_ESPECIALIDADE_SEQ;

-- /*Cria os relacionamentos*/
ALTER TABLE LABDATABASE.MEDICOS ADD CONSTRAINT MEDICOS_ESPECIALIDADE_FK
FOREIGN KEY (ID_ESPECIALIDADE)
REFERENCES LABDATABASE.ESPECIALIDADE (ID_ESPECIALIDADE)
NOT DEFERRABLE;

/*Garante acesso total as tabelas*/
GRANT ALL ON LABDATABASE.PACIENTES TO LABDATABASE;
GRANT ALL ON LABDATABASE.MEDICOS TO LABDATABASE;
GRANT ALL ON LABDATABASE.CONSULTAS TO LABDATABASE;
GRANT ALL ON LABDATABASE.ESPECIALIDADES TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;