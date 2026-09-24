from Produto import Produto


produto1 = Produto("fone de ouvido", 20.00)
produto1.cadastrar()

produto2 = Produto("gabinete", 1880.00)
produto2.cadastrar()

print("====== PRODUTO CADASTRADOS ======")
Produto.listar()