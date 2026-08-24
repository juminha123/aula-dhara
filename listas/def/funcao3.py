def operadores (a,b):
    soma = a + b
    mult = a * b
    return soma, mult
s,m = operadores(4, 12)
print("soma:", s)
print("mult:", m)
print(operadores(32, 45))