# Trabalhando com conjuntos
# Não permite duplicidade
# conjunto = {1, 2, 3, 4, 4, 2} => Só vai imprimir {1, 2, 3, 4}
# conjunto = {1, 2, 3, 4, 4, 2}
# Adicionar um elemento no conjunto
# .add(x) adiciona um elemento no conjunto
# conjunto.add(5)
# Removendo um elemento do conjunto
# .discard(x) remove um elemento do conjunto
# conjunto.discard(1)
# print(type(conjunto))
# print(conjunto)

# Método de união
# .union(var_conjunto) junta os conjuntos em um novo conjunto
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print("União: ", conjunto_uniao)

# Método de intersecção
# .intersection(var_conjunto) pega a intersecção dos dois conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print("Intersecção: ", conjunto_interseccao)

# Diferença
# .difference(var_conjunto) retira os elementos do
# conjunto 1 com base no que está dentro da função
conjunto_diferenca = conjunto.difference(conjunto2)
print("Diferença 1 e 2: ", conjunto_diferenca)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print("Diferença 2 e 1: ", conjunto_diferenca2)

# Diferença simétrica
# .symmetric_difference(var_conjunto) não mostra os elementos
# que existem em ambos os conjuntos
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença simétrica: ", conjunto_diff_simetrica)

# Pertinência
# .issubset(var_conjunto) se os valores do conjunto dentro da função
# estiverem dentro do conjunto referenciado, esse conjunto dentro da
# função é um subconjunto do conjunto refenciado (Precisa ser igual)
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print("Subset: ", conjunto_subset)
# .issuperset(var_conjunto) se o conjunto dentro da função possuir todos
# os valores do conjunto fora da função, esse conjunto da função é um
# superconjunto do conjunto fora da função (Pode ter valores diferentes)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("Superset: ", conjunto_superset)

# Converter uma lista para conjunto
# .set(var_lista) converte a lista para conjunto e tira a duplicidade
lista = ["cachorro", "cachorro", "gato", "vaca"]
conjunto_lista = set(lista)
print("Conjunto => Lista: ", conjunto_lista)

# Converter um conjunto para lista
lista_conjunto = list(conjunto_lista)
print("Lista => Conjunto: ", lista_conjunto)