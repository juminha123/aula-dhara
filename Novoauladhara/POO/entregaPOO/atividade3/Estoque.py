class Estoque:
    def adicionarProduto(self, valor):
        produto = produto + valor
        print("quantidade de produtos atualizada:", produto)
        
    def retirarProduto(self, ValorparaRetirar):
        ValorparaRetirar = int(input("Quantos produtos foram vendidos: "))
        if self.quant >= ValorparaRetirar:
           self.quantidade = self.quantidade - ValorparaRetirar
           print("Ação efetuada com sucesso! a quantidade de produtos atual é de: ", self.quantidade)
        else:
            print("produtos insuficientes insuficiente!")