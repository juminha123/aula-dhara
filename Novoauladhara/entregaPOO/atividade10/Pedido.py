class Pedido:
    def __init__(self, numero, nomeCliente):
        self.numero = numero
        self.nomeCliente = nomeCliente
        self.produtos = []
        self.finalizado = False

                    
    def adicionarProduto(self, produto):
        if not self.finalizado:
            self.produtos.append(produto)
        else:
            print("produto FINALIZADO!")
        
    def calcularValor(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
    
    def status(self):
            self.preparando = True
            print("seu pedido foi finalizado!")
            
    def exibirPedido(self):
        print(f"numero do pedido: {self.numero}")
        print(f"cliente {self.nomeCliente}")
        print(f"Total: {self.calcularValor()}")
        
        if self.finalizado:
          print("status: finalizado")
        else:
            print("status: Aberto")  
