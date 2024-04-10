# yield

'''def generator(n=0):
    yield 1 # pausar
    print('continuando...')
    yield 2
    print('continuando...')
    yield 3
    print('vou terminar')
    return 'Acabou'

gen = generator(n=0)

for n in generator(n=0):
    print(n)
'''

def generator(n=0, maximum=0):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return
        
gen = generator(n=1, maximum=1001)

for n in gen:
    print(n)