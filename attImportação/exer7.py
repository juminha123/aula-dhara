from datetime import datetime
import random


participantes = []

for i in range(5):
    participante = input("nome dos participantes: ")
participantes.append(participante)
print(random.choice(participantes))
data = datetime.now()

print(" O sorteio foi realizado!")
print("Resultado: ", participante," e o sorteio foi feito no dia", data,)

