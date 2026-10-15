from Cliente import Cliente
from Produto import Produto
from Pedido import Pedido


cliente = Cliente("joão")
produto0 = Produto("notebook", 3500)
produto1 = Produto("mouse", 50)

pedido = Pedido(cliente)
pedido.adicionarProduto(produto0)
pedido.adicionarProduto(produto1)

pedido.mostrarPedido()