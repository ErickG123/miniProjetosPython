# Atribuição de variáveis sem tipo
a = 10
b = 10

# Operadores básicos e definição de tipo
soma = int(a + b)
subtracao = int(a - b)
multiplicacao = int(a * b)
divisao = float(a / b)
resto = int(a % b)

# Imprimir um texto
print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
print("Divisão com resto: ", resto)

# type(x) serve para identificar o tipe de alguma variável
print("Tipo da variável soma: ", type(soma))

# Somando uma string com um int
x = "1"
soma2 = int(x) + 1
print("Somando str com int: ", soma2)

# .format(x,x,...) ajuda a concatenar variáveis, para isso é preciso colocar as chaves
print("Soma com format: {}, Subtração com format {}".format(soma, subtracao))

#  Você também pode dar um apelido para a variável
# \n ajuda a quebrar uma linha no terminal na hora de imprimir o texto
print("Soma com format e apelido: {soma}, \nSubtração com format e apelido: {sub}".format(soma=soma, sub=subtracao))

# Diminuindo os prints
print("Soma com format e apelido: {soma}, "
      "\nSubtração com format e apelido: {sub}"
      "\nMultiplicação com format e apelido: {mult}"
      "\nDivisão com format e apelido: {div}".format(soma=soma,
                                                     sub=subtracao,
                                                     div=divisao,
                                                     mult=multiplicacao))

# Pedindo para o usuário informar o valor das variáveis
c = int(input("Digite um número: "))
d = int(input("Digite outro número: "))
somaCInput = c + d
print("Soma dos valores digitados pelo usuário: ", somaCInput)
