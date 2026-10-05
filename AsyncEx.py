# Exemplos de funções assíncronas
import asyncio

async def pikachu():
    print("1 - Pikachu entrou na arena!")
    await asyncio.sleep(2)
    print("2 - Pikachu usou choque do trovão")

async def charmander():
    print("3 - Charmander entrou na arena")
    await asyncio.sleep(3)
    print("4 - Charmander usou brasas")

async def batalha():
    await asyncio.gather(pikachu(), charmander())

asyncio.run(batalha())
print("="* 80)

# Exemplo de requisições assíncronas à APIs:
import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/preco-produto")
async def consultar_precos():
    async with httpx.AsyncClient() as cliente:
        preco1 = client.get("https://api1.com/produto")
        preco2 = client.get("https://api2.com/produto")

        resposta1, resposta2 = await asyncio.gather(preco1, preco2)

    return {
        "api1": resposta1.json(),
        "api2": resposta2.json(),
    }

# Exemplo de uma corrotina:
def minha_corrotina():
    print("Início")
    yield
    print("Depois do yield")

coro = minha_corrotina()
next(coro)   # Início
next(coro)   # Depois do yield

# Segundo exemplo:
async def tarefa1():
    print("Tarefa1 iniciando")
    await asyncio.sleep(2)
    print("Tarefa1 terminando")

async def tarefa2():
    print("Tarefa2 iniciando")
    await asyncio.sleep(1)
    print("Tarefa2 terminando")

async def main():
    await asyncio.gather(tarefa1(), tarefa2())

asyncio.run(main())
