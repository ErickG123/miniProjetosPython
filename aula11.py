# Tratamento de exceções
lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print('Fechando o arquivo')
except ZeroDivisionError: # Tratando exceção de divisão por zero
    print('Não é possível realizar divisão por zero')
    # ArithmeticError é superior ao ZeroDivisionError
except ArithmeticError: # Tratando exceção de número aritiméticos
    print('Houve um erro ao realizar uma operação aritimética')
except IndexError: # Tratando exceção de indice de array inválido
    # Erro genérico
    # print('Erro desconhecido')
    print('Erro ao acessar um indice inválido da lista')
# Tratando exceção de todos os erros
# BaseException é a primeira exceção no topo da hierarquia
except Exception as ex:
    print(ex)
# Executa quando não ocorre exceção
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()