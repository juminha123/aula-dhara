from produto.Produto import Produto


nome = input("insira o nome:")
preco = float(input("insira o preço"))


produto1 = Produto(nome,preco)
produto1.cadastrar()

