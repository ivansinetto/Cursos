'''nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)'''

nomes = ['Maria', 'Helena', 'Luiz']

nome1, *_ = nomes #Variável com _ significa que eu não vou usar essa variável depois
print(nome1)
