class Televisao:
    def __init__(self):
        # var boolean
        self.ligada = False
        self.canal = 5

    def power(self):
        # Testa automaticamente se é True
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

# Quando quem está me chamando for o __main__ (guia do
# mesmo arquivo) eu executo o arquivo, se não for, eu
# não faço nada

# print(__name__)
if __name__ == '__main__':
    tv = Televisao()
    print("TV ligada? :", tv.ligada)
    tv.power()
    print("TV ligada? :", tv.ligada)
    tv.power()
    print("TV ligada? :", tv.ligada)
    print("Canal: ", tv.canal)
    tv.power()
    print("TV ligada? :", tv.ligada)
    tv.aumenta_canal()
    tv.aumenta_canal()
    print("Canal: ", tv.canal)
    tv.diminui_canal()
    tv.diminui_canal()
    tv.diminui_canal()
    print("Canal: ", tv.canal)