# Exercício - sistema de perguntas e respostas
import random

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

perguntas[0].update(Resposta='c')
perguntas[1].update(Resposta='a')
perguntas[2].update(Resposta='b')

while True:
    indice = random.randint(0, len(perguntas) - 1)

    pergunta_escolhida = perguntas[indice]

    print(30 * '-')
    print('Pergunta:', pergunta_escolhida['Pergunta'])

    letras = ['a', 'b', 'c', 'd']
    indice_letras = 0
    for respostas in pergunta_escolhida['Opções']:
        print(letras[indice_letras], ') ', respostas)
        indice_letras += 1

    while True:
        print(30 * '-')
        escolha = input('Escolha uma opção: ').lower()

        if escolha in pergunta_escolhida['Resposta']:
            print('Acertou! 👍')
            break
        else:
            print('Errou ❌')
            continue


#código do professor:
'''
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
'''