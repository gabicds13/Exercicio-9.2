
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API com FastAPI!"}

@app.get("/produtos")
def listar_produtos():
    return {
        "produtos": [
            {"id": 1, "nome": "Notebook", "preco": 3500},
            {"id": 2, "nome": "Mouse", "preco": 80},
            {"id": 3, "nome": "Teclado", "preco": 150}
        ]
    }
