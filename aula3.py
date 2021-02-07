# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))
#
# # Operações condicionais e operadores lógicos
# if a > b and a > c:
#     print("A > B e A > C, valor de A: {}".format(a))
# elif b > a and b > c:
#     print("B > A e B > C, valor de B: {}".format(b))
# else:
#     print("C > A e C > B, valor de C: {}".format(c))
#

# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print("Você digitou pelo menos um número par")
# else:
#     print("Nenhum número par foi digitado")

# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print("Você digitou pelo menos um número par")
# else:
#     print("Nenhum número par foi digitado")

a = int(input("Primeira nota: "))
if a > 10:
    a = int(input("Você digitou errado. Primeira nota: "))

b = int(input("Segunda nota: "))
if b > 10:
    b = int(input("Você digitou errado. Segunda nota: "))

c = int(input("Terceira nota: "))
if c > 10:
    c = int(input("Você digitou errado. Terceira nota: "))

d = int(input("Quarta nota: "))
if d > 10:
    d = int(input("Você digitou errado. Quarta nota: "))

media = (a + b + c + d) / 4
print("Média: {}".format(media))