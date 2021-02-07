# Criar/abrir um arquivo
# open(nome_arq, ação_arq) abre um arquivo e executa alguma ação
# .write(txt) escreve no arquivo
# .close() fecha o arquivo
# .read() lê o arquivo

# Com a letra "w" eu vou conseguir escrever no arquivo
def escrever_arquivo(texto):
    diretorio = 'C:/Users/erick/Documents/GitHub/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

# Com a letra "a" eu vou atualizar o arquivo
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

# Com a letra "r' eu vou ler o arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    # Com o .split('\n') sempre que tiver uma quebra de linha ele vira um item a lista
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        # print(x)
        # Com o .split(',') eu vou seprar o nome do aluno e cada nota em um elemento
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

# Biblioteca responsável por copiar e mover um arquivo
import shutil
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/erick/Documents/GitHub')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/erick/Documents/GitHub/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Cesar, 10, 5, 7, 5\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')