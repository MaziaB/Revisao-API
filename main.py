from fastapi import FastAPI, HTTPException

app = FastAPI()

meus_livrozinhos = {}

@app.get("/Livros")
def get_livros():
    if not meus_livrozinhos:
        return {"message": "Nenhum livro cadastrado"}
    else:
        return {"Livros": meus_livrozinhos}


@app.post("/adiciona")
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    if id_livro in meus_livrozinhos:
        raise HTTPException(status_code=400, detail="Esse livro já está cadastrado!")
    else:
        meus_livrozinhos[id_livro] = {"nome_livro": nome_livro, "autor_livro": autor_livro, "ano_livro": ano_livro}
        return {"message": "Livro adicionado com sucesso!"}


@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    meu_livro = meus_livrozinhos.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado!")
    else:
        if nome_livro:
            meu_livro["nome_livro"] = nome_livro
        if autor_livro:
            meu_livro["autor_livro"] = autor_livro
        if ano_livro:
            meu_livro["ano_livro"] = ano_livro

        return {"message": "As informações do livro foram atualizadas com sucesso!"}


@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in meus_livrozinhos:
        raise HTTPException(status_code=404, detail="Livro não cadastrado")
    else:
        del meus_livrozinhos[id_livro]

    return {"message": "Livro deletado com sucesso!"}
