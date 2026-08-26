nome = input("digite o nome do funcionaria: ")
cargo = input("cargo: ")
salario = float(input("digite o salario: "))

with open("cadastro.txt", "a") as arquivo:
    arquivo.write(f"\n {nome} - {cargo} - R${salario}")
    
#cadastro realizado
print("cadastrado com sucesso")