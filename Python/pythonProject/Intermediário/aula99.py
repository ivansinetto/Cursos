'''from sys import path
import aula99_package.modulo as ap

#print(*path, sep='\n')

print(ap.soma_do_modulo(1, 2))
print(ap.variavel)
print(ap.nova_variavel)'''

'''from aula99_package.modulo import soma_do_modulo, fala_oi

print(__name__)
print(soma_do_modulo(2, 2))
fala_oi()'''

from aula99_package import dobra, soma_do_modulo, nova_variavel, fala_oi

print(dobra(2))
print(soma_do_modulo(2, 3))
print(nova_variavel)
fala_oi()
