import pytest 

# Suponha que temos uma função que registra um Pokemon em um Pokedex:
def registrar_pokemon(pokedex, pokemon):
    pokedex.adicionar(pokemon)

# Queremos testar se a função adicionar foi chamada corretamente. Utilizamos um Mock para isso:
def test_registrar_pokemon(mocker):
    pokedex_mock = mocker.Mock()
    pokemon = {"nome": "Pikachu", "tipo": "Elétrico"}

    registrar_pokemon(pokedex_mock, pokemon)

    pokedex_mock.adicionar.assert_called_once_with(pokemon)


# Suponha que temos uma função que obtém informações de um Pokemon de uma API externa:
def obter_informacoes(api_client, nome_pokemon):
    return api_client.buscar(nome_pokemon)

# Durante os testes, não queremos fazer chamadas reais à API. Utilizamos um Stub para fornecer uma resposta
# predefinida:
def test_obter_informacoes(mocker):
    api_stub = mocker.stub()
    api_stub.buscar.return_value = {"nome": "Charmander", "tipo": "Fogo"}

    resultado = obter_informacoes(api_stub, "Charmander")

    assert resultado["tipo"] == "Fogo"
