# Lambda => Função anônima
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ["cachorro", "gato", "elefante"]
qtd = contador_letras(lista_animais)
print(qtd)

soma = lambda a, b: a + b
subtracao = lambda  a, b: a - b

print(soma(2, 5))
print(subtracao(8, 2))

# Dicionário de funções lambda
calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda  a, b: a * b,
    "divisao": lambda a, b: a / b
}

print(type(calculadora))
# Usando a função lambda do dicionário
soma = calculadora["soma"]
# soma = lambda a, b: a + b
multiplicacao = calculadora["multiplicacao"]
print(soma(10, 5))
print(multiplicacao(10, 3))