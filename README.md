# Sistema de Gestão para Clínica Médica

Este é um projeto disciplinar desenvolvido para a matéria de **Banco de Dados**, orientado pelo professor **Howard Roatti**. O sistema tem como objetivo gerenciar uma clínica médica, permitindo o cadastro e controle de informações como pacientes, médicos, especialidades e consultas.

## Alunos

O projeto foi desenvolvido pelos seguintes alunos:

- **EVE**
- **Wilton Oliveira**
- **Yasmin Neumann**
- **Yasmin Souza**

## Descrição do Projeto

O sistema foi implementado em **Python**, sem o uso de um ORM (Object-Relational Mapping). Toda a interação com o banco de dados é feita utilizando **SQL puro** e o driver **cx_Oracle** para conexão com o banco de dados Oracle.

### Funcionalidades Principais

- **Gestão de Pacientes**: Cadastro, edição, exclusão e consulta de pacientes.
- **Gestão de Médicos**: Cadastro e gerenciamento de médicos e suas especialidades.
- **Agendamento de Consultas**: Registro e controle de consultas médicas.
- **Relatórios**: Geração de relatórios básicos sobre consultas realizadas e pacientes cadastrados.


### Banco de Dados

O banco de dados utilizado para este projeto é o **Oracle**. As operações são realizadas usando **SQL direto**, sem intermediários como ORMs.

As tabelas principais incluem:

- **PACIENTES**: Informações pessoais, CPF, data de nascimento, etc.
- **MEDICOS**: Cadastro de médicos, CRM, especialidade, etc.
- **ESPECIALIDADES**: Lista de especialidades médicas.
- **CONSULTAS**: Agendamento e controle de consultas.

### Scripts SQL

O arquivo `setup.sql` contém os comandos SQL para criação das tabelas necessárias para o sistema. Certifique-se de rodá-lo no banco de dados Oracle antes de utilizar o sistema.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o backend.
- **cx_Oracle**: Driver para conectar o Python ao banco de dados Oracle.
- **Oracle XE**: Sistema de gerenciamento de banco de dados utilizado para armazenar os dados da clínica.

## Pré-requisitos

Antes de começar, você precisará ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html)
- [Git](https://git-scm.com/)

## Configuração do Ambiente

O sistema utiliza um arquivo `.env` para configurar as credenciais de acesso ao banco de dados. Você deve criar um arquivo `.env` na raiz do projeto com o seguinte formato:

### Exemplo de `.env`

```bash
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=1521
DB_SERVICE=XE



