numero = int(input("digite um numero positivo: "))

for i in range(1, numero + 1):
    if i % numero == 0:
        print("primo")
        
    else:
        print("não é primo")