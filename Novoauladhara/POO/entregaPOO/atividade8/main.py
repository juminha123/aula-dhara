from Produto import Produto
from Carrinho import Carrinho


produto1 = Produto("Arroz", 25.00)
produto2 = Produto("feijão", 15.00)
produto3 = Produto("leite", 5.00)

carrinho = Carrinho()

carrinho.adicionarProduto(produto1)
carrinho.adicionarProduto(produto2)
carrinho.adicionarProduto(produto3)
carrinho.removerProduto(produto2)
print("valor da compra: R$", carrinho.calcular())