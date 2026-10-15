from Produto import Produto


for i in range(2):
    print(f"cadastro do produto {i + 1}")
    nome = input("insira o nome:")
    categoria = input("insira a categoria:")
    preco = float(input("insira o preço"))

    produto = Produto(nome, categoria, preco)
    produto.cadastrar()
    
print("produtos cadastrados")
Produto.listar()

idProduto = int(input("digite o ID do produto que deseja excluir: "))
confirmacao = input("confira a exclusão? (s/n):")
if confirmacao.lower() == "s": # ele entende que é a mesma coisa mesmo tendo minusculas ou maiosculas
    excluir = Produto.excluir(idProduto)
    if excluir:
        print("produto excluído com sucesso!")
    else: 
        print("Id não encontrado")
else:
    print("exclusão cancelada")
    
Produto.listar()