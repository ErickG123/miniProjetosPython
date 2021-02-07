# Laços de repetições
# Imprimir os 100 primeiros números
# range() imprime números sequenciais

# Descobrindo se o número é primo
# a = int(input("Digite um número: "))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#        div += 1
# if div == 2:
#     print("Número {} é primo".format(a))
# else:
#     print("Número {} não é primo".format(a))

# Descobrindo os números prime de 0 a tanto
# a = int(input("Digite uma valor: "))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print("Número {} é primo".format(num))

# nota = int(input("Digite uma nota: "))
# while nota > 10:
#     nota = int(input("Nota inválida. Digite uma nota: "))
# print(nota)

# Melhorando a atividade da aula 3
# a = int(input("Primeira nota: "))
# while a > 10:
#     a = int(input("Você digitou errado. Primeira nota: "))
#
# b = int(input("Segunda nota: "))
# while b > 10:
#     b = int(input("Você digitou errado. Segunda nota: "))
#
# c = int(input("Terceira nota: "))
# while c > 10:
#     c = int(input("Você digitou errado. Terceira nota: "))
#
# d = int(input("Quarta nota: "))
# while d > 10:
#     d = int(input("Você digitou errado. Quarta nota: "))
#
# media = (a + b + c + d) / 4
# print("Média: {}".format(media))

a = 100
print(range (1, a-5))