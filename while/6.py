palavra = input("digite um palavra: ")

contador = 0
indice = 0

while indice < len(palavra):
    contador += 1
    indice += 1
print(f"quantidade de letras da palavra {palavra} é: {contador}")