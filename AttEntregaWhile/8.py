numero = int(input("Digite um número: "))
fatorial = 1
 
while numero > 0:
    fatorial = fatorial * numero
    numero -= 1
 
print("o fatorial de", numero, " é ", fatorial)