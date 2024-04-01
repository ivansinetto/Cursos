# Dictionary comprehension e Set comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

'''for chave, valor in produto.items():
    print(chave, valor)'''

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
    if chave != 'categoria'
}

#Tupla
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

ldc = {chave: valor
    for chave, valor in lista
}

# SET
s1 = {2 ** i for i in range(10)}
print(s1)