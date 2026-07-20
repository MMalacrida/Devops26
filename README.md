# Devops26

Projeto desenvolvido nas aulas de DevOps.
A aplicacao e uma API de lista de tarefas feita com FastAPI. Ela permite criar, listar, atualizar e remover tarefas.

## Como executar localmente

Instalar as dependencias:

pip install -r requirements.txt

## Executar a aplicacao:

fastapi run app/main.py

Acessar a documentacao:
http://localhost:8000/docs

## Endpoints principais
GET /tarefas,
POST /tarefas,
PUT /tarefas/{id},
DELETE /tarefas/{id},
GET /metricas,
GET /health

## Tecnologias utilizadas
Python,
FastAPI,
Pytest,
Docker,
GitHub Actions,
Docker Hub,
Kubernetes,
FOSSA

## Pipeline
O projeto possui uma pipeline no GitHub Actions para executar testes, analise estatica, analise de dependencias, build da imagem Docker e implantacao no Kubernetes.
