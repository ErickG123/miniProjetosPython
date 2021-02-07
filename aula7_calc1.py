# Método/Definição
# def soma(a, b):
#     return a + b
#
#
# def subtracao(a, b):
#     return a - b
#
#
# def multiplicacao(a, b):
#     return a * b
#
#
# def divisao(a, b):
#     return a / b


# Chamando o método
# print(soma(1, 2))
# print(subtracao(4, 6))
# print(multiplicacao(2, 2))
# print(divisao(10, 2))

# Classe
class Calculadora:
    # Inicializando valores nessa classe
    # __init__(self) é chamado quando instânciar a classe
    # depois executa o resto dos métodos
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(20, 5)
    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())