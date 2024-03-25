primeiro_valor = float(input('Digite um valor: '))
segundo_valor = float(input('Digite outro valor: '))

if primeiro_valor == segundo_valor:
    print('Os valores são iguais')
elif primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor:.0f} é maior que o segundo valor {segundo_valor:.0f}')
elif primeiro_valor < segundo_valor:
    print(f'O primeiro valor {primeiro_valor:.0f} é menor que o segundo valor {segundo_valor:.0f}')
else:
    print('ERRO: Digite um NÚMERO válido')
