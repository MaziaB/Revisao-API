import pytest

def soma(a,b):
    return a + b

def test_soma_dois_numeros():
    resultado = soma(2,3)
    assert resultado == 5

class TestOperacoesMatematicas:
      def test_soma(self):
         assert soma (1, 2) == 3

      def test_subtracao(self):
         assert 5 - 2 == 3


def multi(a,b):
    return a * b

def test_multi():
    resultado = multi(3,4)
    assert resultado == 12

def div(x,y):
    return x / y

def test_div():
    resultado = div(10,2)
    assert resultado == 5

def test_frase():
    assert "Bruno" in "Meu nome é Bruno"

# Criando um pokemon
# Requisito: Um pokemon deve ter nome, tipo e nível (default = 1)
# 1 - Escrevendo o teste (Red)

def test_criar_pokemon():
    pikachu = Pokemon("Pikachu", "Elétrico")
    assert pikachu.nome == "Pikachu"
    assert pikachu.tipo == "Elétrico"
    assert pikachu.nivel == 1

class Pokemon:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.nivel = 1
        