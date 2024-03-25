import random
import os

facil = ['carro', 'moto', 'batata', 'joelho', 'indio']
medio = ['ventilador', 'cachorro', 'montanha', 'guerreiro', 'caçador']
dificil = ['paralelepipedo', 'artilharia', 'procrastinar', 'oferecimento', 'inconstitucional']
modos = '123'
tentativas = 0
letras_acertadas = ''

print(60 * '-')
print('ADVINHE A PALAVRA \nSelecione um modo de jogo para começar: ')

while True:
    palavra_secreta = ''
    print(' 1 - Fácil \n 2 - Médio \n 3 - Difícil')
    print(60 * '-')

    modo = input('Escolha um modo: ')

    if modo not in modos:
        os.system('cls')
        print('Selecione apenas um número correspondente e tente novamente')
        print(60 * '-')
        continue

    if len(modo) > 1:
        os.system('cls')
        print('Selecione apenas um número correspondente e tente novamente')
        print(60 * '-')
        continue

    if modo == '1':
        palavra_secreta = random.choice(facil)
    elif modo == '2':
        palavra_secreta = random.choice(medio)
    else:
        palavra_secreta = random.choice(dificil)

    print(60 * '-')
    print(f'A palavra secreta tem {len(palavra_secreta)} letras, boa sorte!')

    while True:
        letra_digitada = input('Digite uma letra: ')
        tentativas += 1

        if len(letra_digitada) > 1:
            os.system('cls')
            print('Digite apenas uma letra e tente novamente')
            print(60 * '-')
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        palavra_formada = ''

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print('Palavra formada: ', palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print(60 * '-')
            print('VOCÊ GANHOU!!! PARABÉNS!!!')
            print('A palavra era: ', palavra_secreta)
            print(f'Você teve {tentativas} tentativas, muito bem!')

            while True:
                print(60 * '-')
                jogar_novamente = input('Deseja jogar novamente? (S/N): ')

                if jogar_novamente.upper() == 'S':
                    letras_acertadas = ''
                    tentativas = 0
                    break

                elif jogar_novamente.upper() == 'N':
                    print(60 * '-')
                    print('Obrigado por jogar!')
                    exit()

                else:
                    print('Digite apenas S para sim ou N para não.')
