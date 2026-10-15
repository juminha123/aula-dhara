from Funcionario import Funcionario

nome = input("digite o nome:")
cargo = input("digite o cargo:")
salario = input("digite o salario:")


funcionario = Funcionario(nome, cargo, salario)
funcionario.cadastrar()

idBusca = int(input("digite o ID para buscar: "))
novoNome = input("digite o novo nome: ")
novoCargo = input("digite o novo cargo: ")
novoSalario = float(input("digite o novo salario: "))

alterou = Funcionario.alterar(
    novoNome,
    novoCargo,
    novoSalario,
    idBusca
)
if alterou:
    print(" Funcionario alterado com sucesso!")
else:
    print("ID não encontrado")