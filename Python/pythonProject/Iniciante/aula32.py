"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

while True:
    print(60 * '-')
    try:
        numero_digitado = int(input('Digite um número inteiro para saber se é par ou ímpar: '))
    except ValueError:
        print('ERRO: O valor digitado não é um número inteiro.')
        print('Tente novamente')
        continue

    if (numero_digitado % 2 == 0) == True:
        print(f'O número {numero_digitado}, é Par')
        print(60 * '-')
        break

    else:
        print(f'O número {numero_digitado}, é ìmpar')
        print(60 * '-')
        break


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

while True:
    print(30 * '-')

    try:
        nome = input(str('Qual o seu nome? :'))
    except ValueError:
        print('Digite um nome válido, apenas letras')
        continue

    if nome == '':
        print('Espaço não preenchido \n Tente novamente')
        continue

    try:
        hora_atual = int(input(f'Olá, {nome}! Que horas são? :'))
    except ValueError:
        print('Digite uma hora válida, apenas números')
        continue

    if hora_atual <= 11:
        print(f'Bom dia para você, {nome}! O_O')
        print(30 * '-')
        break

    elif hora_atual <= 17:
        print(f'Boa tarde para você {nome}! ^_^')
        print(30 * '-')
        break

    elif hora_atual <= 23:
        print(f'Boa noite para você {nome}! U_U')
        print(30 * '-')
        break

    else:
        print(f'{hora_atual} horas não é uma hora válida.')
        print('Tente novamente')
        continue

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

while True:
    print(30 * '-')
    try:
        nome = str(input('Escreva seu nome: '))
    except ValueError:
        print('Nome inválido, digite apenas letras.')
        continue

    if nome == '':
        print('Espaço não preenchido \n Tente novamente')
        continue

    elif len(nome) <= 4:
        print(f'Seu nome é curto, {nome}!')
        print(30 * '-')
        break

    elif len(nome) <= 6:
        print(f'Print seu nome é normal, {nome}!')
        print(30 * '-')
        break
    else:
        print(f'Seu nome é muito grande, {nome}!')
        print(30 * '-')
        break

