from fastapi import FastAPI
from datetime import datetime

LISTA_TAREFAS = []
APP = FastAPI()


def nova_tarefa(id: int, titulo: str, descricao: str):
    """Função auxiliar para criar uma tarefa usando dicionário (`dict`)"""
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now()
    }


@APP.get("/")
def index():
    return "Olá, DevOps!"


@APP.get("/tarefas")
def listar_tarefas():
    # Lista tarefas (somente id e titulo)
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS

    tarefas = []

    for tarefa in LISTA_TAREFAS:
        info = {"id": tarefa['id'], "titulo": tarefa['titulo']}
        tarefas.append(info)

    return tarefas


@APP.get("/tarefas/{id}")
def listar_tarefa_especifica(id: int):
    mensagem_padrao = {"mensagem": "Não existe nenhuma tarefa"}

    if len(LISTA_TAREFAS) == 0:
        return mensagem_padrao

    # Busca a tarefa pelo ID
    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id:
            return tarefa

    return mensagem_padrao


@APP.post("/tarefas")
def criar_tarefa(id: int, titulo: str, descricao: str):
    # Verifica se a tarefa já existe
    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id:
            return "TAREFA JÁ EXISTE"

    # Cria uma nova tarefa usando a função nova_tarefa
    tarefa = nova_tarefa(id, titulo, descricao)

    # Adiciona nova tarefa a LISTA_TAREFAS
    LISTA_TAREFAS.append(tarefa)

    return "OK"


@APP.put("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: str, descricao: str, concluido: bool):
    if len(LISTA_TAREFAS) == 0:
        return "TAREFA NÃO EXISTE"

    # Busca a tarefa pelo ID
    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id:
            tarefa["titulo"] = titulo
            tarefa["descricao"] = descricao
            tarefa["concluido"] = concluido

            return "OK"

    return "TAREFA NÃO EXISTE"


@APP.delete("/tarefas/{id}")
def excluir_tarefa(id: int):
    if len(LISTA_TAREFAS) == 0:
        return "TAREFA NÃO EXISTE"

    # Busca a tarefa pelo ID
    for tarefa in LISTA_TAREFAS:
        if tarefa["id"] == id:
            LISTA_TAREFAS.remove(tarefa)

            return "OK"

    return "TAREFA NÃO EXISTE"