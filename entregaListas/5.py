a = int(input("infprme a 1º nota:"))
b = int(input("infprme a 2º nota:"))
c = int(input("infprme a 3º nota:"))

def operadores (a, b, c):
    media = (a + b + c)/3
    return media
m = operadores(a, b, c)
print(m)