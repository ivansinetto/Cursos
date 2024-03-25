# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

'''def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicador(10, 2, 3, 4, 5)
print(multiplicacao)'''


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'O número {numero} é par!'
    return f'O número {numero} é ímpar!'

while True:
    try:
        entrada = int(input('Digite um número para saber se é Par ou Ímpar: '))
    except ValueError:
        print('Digite um número válido e tente novamente.')
        continue
    
    resultado = par_impar(entrada)
    print(resultado)
    break

