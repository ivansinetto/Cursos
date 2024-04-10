#try, except, else, finally

try:
    a = 18
    b = 0
    print('linha 1')
    c = a / b
    print('linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUAR')