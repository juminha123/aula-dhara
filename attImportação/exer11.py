produto = input("cadastre o produto:")
quantidade = input("quantidade: ")
preco = float(input("qual o valor do produto: "))

with open("produto.txt", "a") as arquivo:
    arquivo.write(f"\n {produto} - {quantidade} - R${preco}")
print("cadastrado com sucesso")

with open("produto.txt", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)