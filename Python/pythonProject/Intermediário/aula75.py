# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

'''def duplicar(numero):
    return f'O número {numero} duplicado é: {numero * 2}'

def triplicar(numero):
    return f'O número {numero} triplicado é: {numero * 3}'

def quadruplicar(numero):
    return f'O número {numero} quadruplicado é: {numero * 4}'

n1 = duplicar(5)
n2 = triplicar(5)
n3 = quadruplicar(5)

print(n1)
print(n2)
print(n3)
'''
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))
