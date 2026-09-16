class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos =[]
        
    def adicionarProduto(self, produto):
        self.produtos.append(produto)
        
    def mostrarPedido(self):
        print(f"cliente {self.cliente.nome}")
        print("produtos")
        
        for produto in self.produtos:
            print(
                f" -{produto.nome}"
                f" R$ {produto.preco}")