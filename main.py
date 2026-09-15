from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets
import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./livros.db"

# Criação do bd local
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()

app = FastAPI(
    title="API de Livros",
    description="API para gerenciamento de acervo de bibliotecas",
    version="1.0.0"
)

meus_livrozinhos = {}

class LivroDB(Base):
    __tablename__="Livros"
    id = Column(Integer, primary_key=True, index=True)
    nome_livro = Column(String, index=True)
    autor_livro = Column(String, index=True)
    ano_livro = Column(Integer)

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

Base.metadata.create_all(bind=engine)

def sessao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos!",
            headers={"WWW-Authenticate": "Basic"}
        )


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/Livros")
def get_livros(page: int = 1, limit: int = 10, credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="page ou limit com valores inválidos!")
    
    if not meus_livrozinhos:
        return {"message": "Nenhum livro cadastrado"}

    start = (page - 1) * limit
    end = start + limit

    livros_ordenados = sorted(meus_livrozinhos.items(), key=lambda x: x[0])

    livros_paginados = [
        {"id": id_livro, "nome_livro": livro_data.nome_livro, "autor_livro": livro_data.autor_livro, "ano_livro": livro_data.ano_livro}
        for id_livro, livro_data in livros_ordenados[start:end]
    ]

    return {
        "page": page,
        "limit": limit,
        "total": len(meus_livrozinhos),
        "livros": livros_paginados
    }


@app.post("/adiciona")
def post_livros(id_livro: int, livro: Livro, credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    if id_livro in meus_livrozinhos:
        raise HTTPException(status_code=400, detail="Esse livro já está cadastrado!")
    else:
        meus_livrozinhos[id_livro] = livro
        return {"message": "Livro adicionado com sucesso!"}


@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livro: Livro, credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    meu_livro = meus_livrozinhos.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    else:
        meus_livrozinhos[id_livro] = livro

        return {"message": "As informações do livro foram atualizadas com sucesso!"}


@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int, credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    if id_livro not in meus_livrozinhos:
        raise HTTPException(status_code=404, detail="Livro não cadastrado")
    else:
        del meus_livrozinhos[id_livro]

    return {"message": "Livro deletado com sucesso!"}
