
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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    preco: float

@app.post("/items")
def criar_item(item: Item):
    return {"mensagem": "Item criado com sucesso", "item": item}

@app.put("/items/{item_id}")
def atualizar_item(item_id: int, item: Item):
    return {
        "mensagem": "Item atualizado com sucesso",
        "item_id": item_id,
        "item": item
    }

@app.delete("/items/{item_id}")
def excluir_item(item_id: int):
    return {
        "mensagem": "Item excluido com sucesso",
        "item_id": item_id
    }
