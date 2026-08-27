alunos = input("adicono o nome do aluno: ")

with open("alunos.txt", "a") as arquivo:
    arquivo.write(f"\n{alunos}")
    
print("cadastrado com sucesso")
