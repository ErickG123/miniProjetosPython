# from modulo.py import function
from aula7_tv import Televisao
from aula7_calc1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calc = Calculadora(5, 10)
    print(calc.soma())

    lista = ["cachorro", "gato", "vagalume"]
    total_letras = contador_letras(lista)
    print("Total de letras por palavra da lista: {}".format(total_letras))