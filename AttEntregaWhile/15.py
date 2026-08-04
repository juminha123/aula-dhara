numero = int(input("Digite um número: "))
 
contador = 1
divisores = 0
 
while contador <= numero:
    if numero % contador == 0:
        divisores += 1
    contador += 1
 
if divisores == 2:
    print("É primo")
