class Boletim:
    def __init__(self,nome,):        
        self.nome = nome
        self.notas = [] 
        
    def adicionarNotas(self, nota):
       self.notas.append(nota)
    
    def media(self):
        soma = sum(self.notas) #soma todas as notas
        return soma / len(self.notas) #len passa uma por uma e faz a média
    
    def verificarSituacao(self):
        media = self.media()
        print(f"Aluno: {self.nome}")
        print(f"Média: {media}")
        
        if media >= 7:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")