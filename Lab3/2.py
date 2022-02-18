def func(a, b):
    print(a + b)
func(45, 98)

def func(name):
    print(f'Hi {name}') #or print('Hi' + name)
func('Almaty')

def func(a, b):
    print(a + b)
func( '595', '2')    

def func(a: int, b: int) -> float:
    return float(a + b)
c = func(23, 47)
print(c)   