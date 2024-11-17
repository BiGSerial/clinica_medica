# Sistema de Gestão para Clínica Médica

Este é um projeto disciplinar desenvolvido para a matéria de **Banco de Dados**, orientado pelo professor **Howard Roatti**. O sistema tem como objetivo gerenciar uma clínica médica, permitindo o cadastro e controle de informações como pacientes, médicos, especialidades e consultas.

## Alunos

O projeto foi desenvolvido pelos seguintes alunos:

- **Catharina Alves**
- **Eve Chalabi**
- **Wilton Oliveira**
- **Yasmin Neumann**
- **Yasmin Sousa**

## Descrição do Projeto

O sistema foi implementado em **Python**, utilizando o banco de dados **MongoDB** para armazenamento de informações. Todas as operações de banco de dados são realizadas utilizando a biblioteca **PyMongo**.

### Funcionalidades Principais

- **Gestão de Pacientes**: Cadastro, edição, exclusão e consulta de pacientes.
- **Gestão de Médicos**: Cadastro e gerenciamento de médicos e suas especialidades.
- **Agendamento de Consultas**: Registro e controle de consultas médicas.
- **Relatórios**: Geração de relatórios básicos sobre consultas realizadas e pacientes cadastrados.

### Banco de Dados

O banco de dados utilizado para este projeto é o **MongoDB**, um banco de dados NoSQL orientado a documentos.

As coleções principais incluem:

- **pacientes**: Informações pessoais, CPF, data de nascimento, etc.
- **medicos**: Cadastro de médicos, CRM, especialidade, etc.
- **especialidades**: Lista de especialidades médicas.
- **consultas**: Agendamento e controle de consultas.

### Scripts de Configuração

O arquivo `setup_database.py` na pasta `src/app/` contém a configuração inicial das coleções no MongoDB, incluindo a inserção de dados de exemplo.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o backend.
- **PyMongo**: Driver para conectar o Python ao banco de dados MongoDB.
- **MongoDB**: Sistema de gerenciamento de banco de dados utilizado para armazenar os dados da clínica.

## Pré-requisitos

Antes de começar, você precisará ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [MongoDB](https://www.mongodb.com/try/download/community)
- [Git](https://git-scm.com/)




