# API de Cadastro de Alunos

## Descrição

Este projeto consiste no desenvolvimento de uma API REST utilizando Python com o framework FastAPI. A aplicação permite o cadastro e a listagem de alunos, conforme os requisitos propostos na atividade.

---

## Objetivo da Atividade

Implementar:

* Uma entidade Aluno
* Um DTO (Data Transfer Object) para entrada de dados
* Uma API para cadastro de alunos
* Uma API para listagem de alunos
* Persistência em memória utilizando um array
* Criação de 5 alunos distintos

---

## Estrutura do Projeto

O projeto foi desenvolvido em um único arquivo (`main.py`) contendo:

* Definição da API
* Modelagem da entidade
* Definição do DTO
* Estrutura de armazenamento
* Endpoints

---

## Tecnologias Utilizadas

* Python
* FastAPI
* Uvicorn

---

## Modelagem

### Entidade: Aluno

A entidade representa o modelo interno do sistema, contendo os atributos:

* nome
* cpf
* endereco
* curso

Essa estrutura é utilizada para armazenar os dados dentro da aplicação.

---

### DTO: AlunoDTO

O DTO (Data Transfer Object) foi utilizado para receber e validar os dados de entrada da API.

Ele garante que os dados enviados pelo cliente estejam no formato correto antes de serem processados.

---

## Persistência de Dados

Os dados são armazenados em memória utilizando uma lista (array):

```python
alunos = []
```

Essa abordagem foi adotada conforme solicitado no enunciado da atividade.

---

## Funcionalidades da API

### 1. Cadastro de Aluno

**Endpoint:** `POST /alunos`

Responsável por receber os dados de um aluno, validar via DTO, converter para entidade e armazenar no array.

Exemplo de entrada:

```json
{
  "nome": "Zara",
  "cpf": "12345678900",
  "endereco": "Rua Teste",
  "curso": "Sistemas para Internet"
}
```

---

### 2. Listagem de Alunos

**Endpoint:** `GET /alunos`

Retorna todos os alunos cadastrados no sistema.

Os dados são convertidos de objeto (entidade) para formato JSON antes da resposta.

---

## Inicialização com Dados

Para atender ao requisito da atividade, foram criados 5 alunos automaticamente na inicialização da aplicação utilizando o evento de startup.

---

## Como Executar o Projeto

1. Instalar dependências:

```
pip install fastapi uvicorn
```

2. Executar a aplicação:

```
uvicorn main:app --reload
```

3. Acessar no navegador:

```
http://127.0.0.1:8000/docs
```

---

## Considerações Finais

O projeto atende a todos os requisitos propostos, incluindo:

* Separação entre DTO e entidade
* Implementação de endpoints REST
* Persistência em memória
* Inicialização com dados
* Estrutura clara e funcional

A aplicação foi desenvolvida com foco em organização, clareza e boas práticas iniciais de desenvolvimento de APIs.

