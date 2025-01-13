import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.models import *
import app.db.session as db
import typing


app = FastAPI()
#hosts que são permitidos a acessar a API
origins = [
    "http://localhost:3000", 
]
#adiciona middleware
app.add_middleware(
    #Adicionando CORS
    CORSMiddleware,
    #Permitir todos os hosts em origins
    allow_origins=origins,
    #Permitir credenciais, como tokens, cookies e autorizações no geral
    allow_credentials=True,
    #Metodos HTTP permitidos
    allow_methods=["*"],
    #Headers HTTP permitidos
    allow_headers=["*"],
)

#Rota GET para obter todas as frutas
#response_model=Fruits converte a resposta em um objeto Json baseado em Fruits
@app.get("/fruits")
async def get_fruits() -> Fruits:
    return Fruits(fruits=db.get_fruits())

@app.get("/fruits/{name}")
async def get_fruit(name: str) -> Fruit:
    if db.fruit_exists(name):
        return Fruit(name=name)
    raise HTTPException(status_code=404, detail="Fruit not found")

#Rota POST para adicionar uma nova fruta
#response_model=Fruits converte a resposta em um objeto Json baseado em Fruit
#fruit:Fruit indica que o objeto Json a ser adicionado deve ser baseado em Fruit
@app.post("/fruits", response_model=Fruit)
async def add_fruit(fruit: Fruit):
    db.memory_db["fruits"].append(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
