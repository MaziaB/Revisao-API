import pytest 

# Fixture para o Pikachu
@pytest.fixture
def pikachu():
    return {"nome": "Pikachu", "tipo": "Elétrico", "nível": 15}

# Fixture para o Charmander
@pytest.fixture
def charmander():
    return {"nome": "Charmander", "tipo": "Fogo", "nível": 12}

# Teste que utiliza ambas as fixtures
def test_batalha_pokemon(pikachu, charmander):
    assert pikachu["nível"] > charmander["nível"]
