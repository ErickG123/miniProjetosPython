# Classe
# Nesse caso você não vai instaciar o valor na classe
# você vai instacionar o valor no método da classe
class Calculadora:
    # Inicializando valores nessa classe
    # __init__(self) é chamado quando instânciar a classe
    # depois executa o resto dos métodos
    # pass faz com que não de erro por estar vazio
    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 5))
print(calculadora.subtracao(10, 5))
print(calculadora.multiplicacao(10, 5))
print(calculadora.divisao(10, 5))