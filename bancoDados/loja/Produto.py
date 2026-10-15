from produto.conexao import conectar

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        
    def cadastrar(self): # CADASTRAR UM PRODUTO
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos(nome, preco) VALUES (%s, %s)"
        valores = (self.nome, self.preco)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("produto cadastrado!")