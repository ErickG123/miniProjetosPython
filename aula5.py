# Trabalhando com listas
# Listas são mutáveis
# var = [...] define uma lista
lista = [12, 10, 7, 5, 100]
lista_animais = ["cachorro", "gato", "elefante", "lobo", "arara", "abutre", "zebra"]

# print(lista_animais[1])

# lista_animais[0] = "macaco"
# print(lista_animais)

# for x in lista_animais:
#     print(x)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# sum() soma todos os valores da lista
# print(sum(lista))

# max() busca o maior valor da lista
# print(max(lista))

# min() busca o menor valor da lista
# print(min(lista))

# Funciona para lista de texto também, ele pega em ordem alfabética
# print(max(lista_animais))
# print(min(lista_animais))

# Verificando se tem um elemento na lista
# if "gato" in lista_animais:
#     print("Existe")
# else:
#     print("Não existe")

# Multiplicar listas
# nova_lista = lista_animais * 3
# print(nova_lista)

# Incluindo valores que não existe na lista
# .append() vai adicionar um novo elemento na lista
# if "vaca" in lista_animais:
#     print("Existe um vaca")
# else:
#     print("Não existe um vaca")
#     lista_animais.append("vaca")
#     print(lista_animais)

# Retirando valores de uma lista
# .pop() vai retirar o último valor da lista se não informar nada
# .pop(x) tira o valor da posição x da lista
# lista_animais.pop()
# print(lista_animais)

# Retirando valores de uma lista através do nome
# lista_animais.remove("elefante")
# print(lista_animais)

# Ordenando uma lista
# .sort() ordena a lista em ordem crescente para números
# .sort() ordena a lista de A a Z para textos
# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)

# .reverse() faz lista começar do final
# lista.reverse()
# lista_animais.reverse()
# print(lista_animais)
# print(lista)

# Trabalhando com tuplas
# Tuplas são imutáveis
# var = (...) define um tupla
# len() serve para ver quantos registros eu tenho na lista ou na tupla
tupla = (1, 10, 12, 14)
# print(tupla[0])
# print(len(tupla))

# Convertendo uma lista para uma tupla
# tuple(var_list) transforma a lista em tupla
tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)

# Convertendo uma tupla para uma lista
# list(var_tuple) transforma a tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)