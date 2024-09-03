# biblioteca
import os
from datetime import date

# entrada de dados
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
data = f'{date.today().day}/{date.today().month}/{date.today().year}'

# limpa tela
os.system('cls')

# Loop 
while True:
    
    # Lista de filme
    print(f'{'='*30} Filmes em Cartaz e sua classificação indicativas {'='*30}')
    print(f'{data}\n')
    print('SALA 1 - Veloses e Furiosos / 16 anos')
    print('SALA 2 - Invocação do mal 3 / 18 anos')
    print('SALA 3 - Minions / Livre')
    print('SALA 4 - Bad Boys 4 / 14 anos')
    print('SALA 5 - Vovó Zona / 10 anos')

    # selecione o filme
    sala = input('\nQual filme deseja?: ')

    #limpa tela
    os.system('cls')

    match sala:
        case '1':
            idade_minima = 16
            filme = 'Veloses e Furiosos'
        case '2': 
           idade_minima = 18
           filme = 'Invocação do mal'
        case '3': 
           idade_minima = 0
           filme = 'Minions'
        case '4': 
           idade_minima = 16
           filme = 'Bad Boys 4'
        case '5': 
           idade_minima = 10
           filme = 'Vovó Zona'
        case _:
            print('Sala inexistente, favor escolher outra sala')
    
    # verificação de idade
    if idade >= idade_minima:
        # Ingresso
        print(f'Ingresso impresso no dia: {data}.\n')
        print(f'Pagante: {nome}.')
        print(f'Filme: {filme},')
        print(f'Sala: {sala}.')
        print(f'\n Tenha um ótimo filme.')
        break
    else:
        print(f'{nome} não possui a idade mínima para ver {filme}.')
        print('Favor escolher outro filme.')
    
    