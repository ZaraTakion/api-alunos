from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# DTO (entrada de dados)
class AlunoDTO(BaseModel):
    nome: str
    cpf: str
    endereco: str
    curso: str

# Entidade (modelo interno)
class Aluno:
    def __init__(self, nome, cpf, endereco, curso):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.curso = curso

# "Banco de dados" em memória
alunos = []

# Criar 5 alunos automaticamente ao iniciar
@app.on_event('startup')
def criar_alunos_iniciais():
    alunos.append(Aluno('João Silva', '11111111111', 'Rua A', 'ADS'))
    alunos.append(Aluno('Maria Souza', '22222222222', 'Rua B', 'Engenharia'))
    alunos.append(Aluno('Carlos Lima', '33333333333', 'Rua C', 'Direito'))
    alunos.append(Aluno('Ana Costa', '44444444444', 'Rua D', 'Medicina'))
    alunos.append(Aluno('Pedro Rocha', '55555555555', 'Rua E', 'Arquitetura'))

# Endpoint de cadastro
@app.post('/alunos')
def cadastrar_aluno(aluno_dto: AlunoDTO):
    aluno = Aluno(
        nome=aluno_dto.nome,
        cpf=aluno_dto.cpf,
        endereco=aluno_dto.endereco,
        curso=aluno_dto.curso
    )

    alunos.append(aluno)

    return {'mensagem': 'Aluno cadastrado com sucesso'}

# Endpoint de listagem
@app.get('/alunos')
def listar_alunos():
    resultado = []

    for aluno in alunos:
        resultado.append({
            'nome': aluno.nome,
            'cpf': aluno.cpf,
            'endereco': aluno.endereco,
            'curso': aluno.curso
        })

    return resultado