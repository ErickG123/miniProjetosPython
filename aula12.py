import requests

# Requisição HTTP
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dado_cep = response.json()
    print(dado_cep['logradouro'])
    print(dado_cep['complemento'])
    return dado_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    reponse = requests.get(url)
    return reponse.text

if __name__ == '__main__':
    response = retorna_response('https://youtube.com')
    print(response)
    # retorna_dados_cep('22041001')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites'] ['front_shiny'])