# Pegando a data atual
from datetime import date, datetime, time, timedelta

def trab_data():
    # Traz a data de hoje
    data_atual = date.today()
    print(data_atual)
    # Colocando no formato brasileiro
    # ..strftime(date) para formatar a data
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d-%m-%Y'))
    print(type(data_atual))

    # Data com string por causa da formatação
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))

    # Data com string por causa da formatação
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trab_time():
    # Criando horas
    # Por causa da conversão a data virou uma string
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))

def trab_datetime():
    # Data e hora atual
    data_atual = datetime.now()
    print(data_atual)
    # Só a data
    print(data_atual.strftime('%d/%m/%Y'))
    # Só o horário
    print(data_atual.strftime('%H:%M:%S'))
    # DiaSemana/Mês/Dia/Hora/Ano
    print(data_atual.strftime('%c'))
    # Dia
    print(data_atual.day)
    # Mês
    print(data_atual.month)
    # Ano
    print(data_atual.year)
    # Hora
    print(data_atual.hour)
    # Data
    print(data_atual.date())
    # Dia da Semana
    print(data_atual.weekday())
    # Dia da Semana traduzida
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    # Criando uma data
    data_criada = datetime(2021, 2, 8, 1, 41, 50)
    print(data_criada)
    print(data_criada.strftime('%c'))
    # String para datetime
    data_string = '01/01/2021'
    # .strptime(date, format) converte a var str em datetime
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))
    print(data_convertida.weekday())
    # Soma e subtração de data
    # timedelta(days=x) tira a quantidade de dias que você passou
    # timedelta(hours=x) tira a quantidade de horas que você passou
    # timedelta(minutes=x) tira a quantidade de minuitos que você passou
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    # trab_data()
    # trab_time()
    trab_datetime()