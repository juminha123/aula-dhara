import random
chute = int(input("tente adivinhar um numero de 1 a 20: "))

numero = random.randint(1,20)
print(numero)

if chute == numero:
    print("parabens vc acertou!")
elif chute < numero:
    print("Chutou baixo")
else:
    print("maior doque precisava!")