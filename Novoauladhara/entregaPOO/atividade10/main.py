from Produto import Produto
from Pedido import Pedido


produto1 = Produto("Pizza", 12.00)
produto2 = Produto("Suco Natural", 7.00)
produto3 = Produto("petit gatôt", 30.00)

pedido = Pedido(1, "Amanda")

pedido.adicionarProduto(produto1)
pedido.adicionarProduto(produto2)
pedido.adicionarProduto(produto3)

pedido.exibirPedido()
pedido.status()
