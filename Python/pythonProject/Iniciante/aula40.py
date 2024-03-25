numeros_validos = None
operadores_validos = '+-/*'

while True:
    print(30 * '-')

    #Configuraçôes do primeiro número abaixo
    numero1 = input('Digite um número: ')
    try:
        numero1_float = float(numero1)
        numeros_validos = True
    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print('Primeiro número inválido, tente novamente.')
        continue

    #Configurações do operador abaixo
    operador = input('Digite um operador (+-/*): ')

    if operador not in operadores_validos:
        print('operador inválido, tente novamente.')
        continue

    #Configurações do segundo número abaixo
    numero2 = input('Digite outro número: ')

    try:
        numero2_float = float(numero2)
        numeros_validos = True
    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print('Segundo número inválido, tente novamente.')
        continue

    #Configurações de cálculo abaixo
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        resultado = numero1_float + numero2_float
        print(f'Resultado: {resultado}')
        print(30 * '-')

    elif operador == '-':
        resultado = numero1_float - numero2_float
        print(f'Resultado: {resultado}')
        print(30 * '-')

    elif operador == '/':
        resultado = numero1_float / numero2_float
        print(f'Resultado: {resultado}')
        print(30 * '-')

    elif operador == '*':
        resultado = numero1_float * numero2_float
        print(f'Resultado: {resultado}')
        print(30 * '-')

    else:
        print('Deu ruim aqui') #O código não pode chegar aqui

    #Seleção de saída
    sair = input('Quer [S]air? :').lower().startswith('s')

    if sair:
        print(30 * '-')
        print('Até mais! (～￣▽￣)～')
        break


#Sugestão da IA Gemini:

"""
Seu código parece estar bom e deve funcionar corretamente para realizar operações básicas de calculadora. Aqui estão 
algumas sugestões de melhoria:

Trate de erros de divisão por zero: Adicione uma verificação para garantir que o denominador (número2) não seja zero
antes de executar a divisão.

Use um loop while True para repetir o programa: Em vez de usar várias instruções continue para retornar ao início do 
loop, você pode usar um loop while True e usar break para sair do loop quando necessário.

Simplifique a verificação de números válidos: Você pode simplificar a verificação de números válidos usando uma única 
instrução try-except para verificar se ambos os números podem ser convertidos para float.

Use funções: Você pode refatorar seu código em funções separadas para melhorar a legibilidade e a manutenção. 
Por exemplo, você pode ter uma função para obter um número válido do usuário, uma função para verificar o operador e 
uma função para realizar o cálculo.

Aqui está um código Python otimizado com base nas sugestões acima:"""

def obter_numero_valido():
    while True:
        numero = input("Digite um número: ")
        try:
            numero_float = float(numero)
            return numero_float
        except ValueError:
            print("Número inválido, tente novamente.")

def obter_operador_valido():
    while True:
        operador = input("Digite um operador (+-/*): ")
        if operador in operadores_validos:
            return operador
        else:
            print("Operador inválido, tente novamente.")

def realizar_calculo(numero1, operador, numero2):
    if operador == '+':
        resultado = numero1 + numero2
    elif operador == '-':
        resultado = numero1 - numero2
    elif operador == '/':
        if numero2 == 0:
            print("Divisão por zero não é permitida.")
            return None
        resultado = numero1 / numero2
    elif operador == '*':
        resultado = numero1 * numero2
    return resultado

# Programa principal
while True:
    print(30 * "-")
    numero1 = obter_numero_valido()
    operador = obter_operador_valido()
    numero2 = obter_numero_valido()
    resultado = realizar_calculo(numero1, operador, numero2)
    if resultado is not None:
        print(f"Resultado: {resultado}")
    print(30 * "-")
    sair = input("Quer sair? (S/N): ").lower().startswith("s")
    if sair:
        print(30 * "-")
        print("Até mais!")
        break