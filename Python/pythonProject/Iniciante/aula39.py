"""
Iterando strings com while
"""

print(40 * '-')
while True:
    try:
        nome = str(input('Qual o seu nome? :'))
    except ValueError:
        print('Digite um nome válido')
        continue

    indice = 0
    novo_nome = ''

    while indice < len(nome):
        letra = nome[indice]
        novo_nome += f'*{letra}'
        indice += 1

    novo_nome += '*'
    print(novo_nome)
    print(40 * '-')
    break
