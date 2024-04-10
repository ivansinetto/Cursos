#try, except, else, finally
try:
    print('ABRIR ARQUIVO')
    #8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
except IndexError:
    print('IndexError')
except (NameError, ImportError) as error:
    print(error.__class__.__name__)
    print(error)
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
