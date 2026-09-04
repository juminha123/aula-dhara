#animal será a classe "pai"
class Animal:
    def __init__(self,nome):
        self.nome = nome
    def apresentar (self):
        print("O animal se chama", self.nome)
    def emitir_som(self):   
        print("o animal emitiu um som")