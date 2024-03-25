# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

del pessoa['sobrenome']

print(pessoa)

pessoa[chave] = 'Ivan Neto'

print(pessoa)

if pessoa.get('Sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
