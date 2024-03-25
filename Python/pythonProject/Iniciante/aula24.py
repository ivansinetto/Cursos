#Operadores in e not in
#Strings são iteráveis
# 0 1 2 3 4 5
# o t á v i o
#-6-5-4-3-2-1
#print(nome[2])

'''
nome = 'Otávio'
print('vio' in nome)
print('Ivan' not in nome)
'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
