"""
Assignment: Building REST APIs with FastAPI
============================================

Instalação das dependências:
    pip install fastapi uvicorn

Para executar a API:
    uvicorn main:app --reload

Depois acesse a documentação interativa em: http://127.0.0.1:8000/docs
(Dica: renomeie este arquivo para main.py ou ajuste o comando acima)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API", description="API REST para gerenciar livros")


# Modelo Pydantic usado para validar o corpo das requisições (Tarefa 3)
class Book(BaseModel):
    title: str
    author: str
    year: int


# "Banco de dados" em memória — use esta lista nos seus endpoints
books = [
    {"id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"id": 2, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
]


# ----------------------------------------------------------------------
# Tarefa 1: GET /books — retorne a lista completa de livros
# ----------------------------------------------------------------------
# @app.get("/books")
# def list_books():
#     ...


# ----------------------------------------------------------------------
# Tarefa 2: GET /books/{book_id} — retorne um livro pelo ID
# Dica: use HTTPException(status_code=404, detail="Book not found")
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Tarefa 3: POST /books — crie um novo livro (status 201)
# Dica: receba um parâmetro do tipo Book e gere o id automaticamente
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Tarefa 4: PUT /books/{book_id} e DELETE /books/{book_id}
# Dica: DELETE deve retornar status 204 (sem corpo de resposta)
# ----------------------------------------------------------------------
