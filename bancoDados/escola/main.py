from Aluno import Aluno


print("-------- CADASTRO DE ALUNO ---------")
nome = input("digite o nome do aluno: ")
idade = int(input("digite a idade: "))
curso= input("digite o curso: ")

aluno1 = Aluno(nome, idade, curso)
aluno1.cadastrar()
print("------------- ALUNOS CADASTRADOS ----------------")
Aluno.listar()