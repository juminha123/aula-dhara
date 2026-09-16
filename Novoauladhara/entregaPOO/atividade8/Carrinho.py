class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def adicionarProduto(self,produto):
        self.produtos.append(produto)
    def removerProduto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            print("Produto Removido")
        else:
            print("não tem produto")
        
    def calcular(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total