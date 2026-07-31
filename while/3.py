numero = int(input("digite um numero: "))

contador = 1
# enquanto o contador for >= a 10
while contador <= 10:
    res = contador * numero
    print(f"{numero} X {contador} = {res}")
    contador += 1