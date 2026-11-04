# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Os alunos aprenderão a construir APIs REST usando o framework FastAPI, criando endpoints para listar, criar, atualizar e remover recursos (operações CRUD) com validação de dados usando Pydantic.

## 📝 Tasks

### 🛠️ Criar seu Primeiro Endpoint

#### Descrição
Usando o starter code fornecido, crie um endpoint `GET /books` que retorne a lista completa de livros armazenada em memória. Execute a API com `uvicorn` e teste o endpoint pela documentação interativa em `/docs`.

#### Requisitos
O programa concluído deve:

- Expor o endpoint `GET /books` retornando a lista de livros em formato JSON
- Retornar status HTTP `200` na resposta
- Ser executável com `uvicorn main:app --reload`

Exemplo de resposta:

```json
[
  { "id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943 }
]
```

### 🛠️ Buscar um Livro pelo ID

#### Descrição
Crie um endpoint `GET /books/{book_id}` que receba o ID do livro como parâmetro de rota e retorne apenas o livro correspondente. Trate o caso em que o livro não existe.

#### Requisitos
O programa concluído deve:

- Receber `book_id` como parâmetro de rota do tipo inteiro
- Retornar o livro correspondente com status `200` quando encontrado
- Retornar status `404` com a mensagem `{"detail": "Book not found"}` quando o ID não existir (use `HTTPException`)

### 🛠️ Criar Novos Livros com Validação

#### Descrição
Crie um endpoint `POST /books` que receba os dados de um novo livro no corpo da requisição. Use o modelo Pydantic `Book` fornecido no starter code para validar os dados automaticamente.

#### Requisitos
O programa concluído deve:

- Aceitar um JSON com os campos `title`, `author` e `year` no corpo da requisição
- Gerar o `id` do novo livro automaticamente (maior ID existente + 1)
- Adicionar o livro à lista em memória e retorná-lo com status `201`
- Rejeitar automaticamente requisições com campos faltando ou de tipo inválido (validação do Pydantic)

Exemplo de requisição:

```json
{ "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899 }
```

### 🛠️ Completar o CRUD: Atualizar e Remover

#### Descrição
Finalize a API implementando os endpoints `PUT /books/{book_id}` para atualizar um livro existente e `DELETE /books/{book_id}` para removê-lo. Ao concluir, sua API terá todas as operações CRUD de uma API REST completa.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` que substitui os dados do livro e retorna o livro atualizado com status `200`
- Implementar `DELETE /books/{book_id}` que remove o livro e retorna status `204` sem corpo de resposta
- Retornar status `404` em ambos os endpoints quando o livro não existir
- Manter todos os endpoints anteriores funcionando corretamente
