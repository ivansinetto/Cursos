# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda ',
}

#print(p1['nome'])
#print(p1.get('nome', 'None'))

#nome = p1.pop('nome')
#ultima_chave = p1.popitem()
#print(nome)
#print(p1)

p1.update({
    'nome': 'Ivan Neto',
    'idade': '22',
})
print(p1)

p1.update(nome='Ivan', sobrenome='Neto', idade=23)
print(p1)

p1.pop('sobrenome')
tupla = (('nome', 'Lavinia'), ('idade', 19))
p1.update(tupla)
print(p1)

lista = [['nome', 'Biannca'], ['idade', 14]]
p1.update(lista)

print(p1)
