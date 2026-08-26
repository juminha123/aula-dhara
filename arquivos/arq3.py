nome = input("digite o nome do funcionaria: ")
cargo = input("cargo: ")

with open("colaboradores.txt", "a") as arquivo:
    #salva as informações no arquivo
    arquivo.write(f"\n nome é {nome} e seu cargo é {cargo}")
print("colaboradores cadastrados")
with open("colaboradores.txt", "r") as arquivo:
    #exibir todo o conteudo do arquivo
    print(arquivo.read())