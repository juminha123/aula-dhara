class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")    
        print(f"Nota: {self.nota}")    
