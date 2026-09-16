class Produto:
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco 
        self.quantidade = quantidade
        
    def apresentar(self):
        print(f"produto: {self.nome}")    
        print(f"Seu valor é de: {self.preco}")
        print(f"Tem: {self.quantidade} no estoque")
    
    def adicionarProduto(self):
        valor = int(input("Quantos produtos foram adicionados: "))
        self.quantidade = self.quantidade + valor
        print("quantidade de produtos atualizada:", self.quantidade)
        
    def retirarProduto(self):
        ValorparaRetirar = int(input("Quantos produtos foram vendidos: "))
        if self.quantidade >= ValorparaRetirar:
           self.quantidade = self.quantidade - ValorparaRetirar
           print("Ação efetuada com sucesso! a quantidade de produtos atual é de: ", self.quantidade)
        else:
            print("produtos insuficientes insuficiente!")
            
    def valordeEstoque(self):
         return self.quantidade * self.preco
       
        #print(f"O valor total em estoque é de: {valorEstoque}")