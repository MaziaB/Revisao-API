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
