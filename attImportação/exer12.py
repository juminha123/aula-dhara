nome = input("digite o nome do funcionaria: ")
idade = input("idade: ")
profissao = input("profissão: ")

with open("cadastro.txt", "a") as arquivo:
    arquivo.write("o nome do usuário é", nome, "vc trabalha como", profissao, " e tem", idade,"anos")
print("cadrasto realizado")
with open("cadastro.txt", "r") as arquivo:
    print(arquivo.read())