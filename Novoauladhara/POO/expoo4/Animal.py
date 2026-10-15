class Animal:
    def __init__(self,nome):
        self.nome = nome
    def emitir_som(self):   
        print("o animal emitiu um som")
    def apresentar (self):
        print("O animal se chama", self.nome)