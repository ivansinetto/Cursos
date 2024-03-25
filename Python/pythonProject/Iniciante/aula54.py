import os

lista = []

while True:
    print(40 * '-')
    if lista == []:
        print('A sua lista está vazia')
        print(40 * '-')

    else:
        print('Itens da sua Lista:\t [Índice/Nome]')
        for indice, nome in enumerate(lista):
            print(indice,'|', nome,)

    selecao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if len(selecao) > 1:
        os.system('cls')
        print('Selecione apenas uma letra')
        continue

    if selecao.startswith('i'):
        print(40 * '-')
        inserir = input('Digite o que deseja inserir: ')

        if inserir == '':
            os.system('cls')
            print('Você não digitou um valor, tente novamente')
            continue

        lista.append(inserir)
        os.system('cls')

    elif selecao.startswith('a'):
        print(40 * '-')
        apagar = input('Digite o índice do item que deseja apagar: ')

        try:
            apagar_int = int(apagar)
        except ValueError:
            os.system('cls')
            print('Digite apenas o número que corresponde ao índice do ítem que deseja apagar\nTente novamente')
            continue

        del lista[apagar_int]

    elif selecao.startswith('l'):
        os.system('cls')
        continue

    elif selecao.startswith('s'):
        print(40 * '-')
        print('Até mais!')
        exit()

    else:
        print('Digite uma opção válida e tente novamente.')
        continue
