class Personagem:
    def __init__(self, nome, vida,forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        
    def atacar(self, alvo):
        alvo.vida -= self.forca
        if alvo.vida < 0:
            alvo.vida = 0
        print(f"{self.nome} atacou {alvo.nome}")
        print(f"{alvo.nome} perdeu {self.forca} de vida")
        
    def exibirVida(self):
        print(f"{self.nome} possui {self.vida} de vida")