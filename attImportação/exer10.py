mensagem = input("adicione a mensagem que deseja adicionar: ")
with open("mensagem.txt", "a") as arquivo:
    arquivo.write(mensagem)
print("mensagem adiconada")
with open("mensagem.txt", "r") as arquivo:
    print(arquivo.read())