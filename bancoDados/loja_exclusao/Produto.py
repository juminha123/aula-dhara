from conexao import conectar

class Produto:
    def __init__(self,nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
    
    def cadastrar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
            INSERT INTO produtos(nome, categoria, preco)
            VALUES(%s, %s, %s)"""
        valores = (self.nome,self.categoria, self.preco)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("produto cadastrado com sucesso")
        
    @staticmethod #listar e buscar por id
    
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        produtos = cursor.fetchall() #lista para banco de dados
        
        for produto in produtos:
            print(
                f"id {produto[0]}|"
                f"nome {produto[1]}|"
                f"categoria {produto[2]}|"
                f"preço {produto[3]}|"
            )
        cursor.close()
        conexao.close()
        
    #tudo que tem parenteses é uma função
    @staticmethod
    def excluir(idProduto):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produto WHERE id = %s", (idProduto,)) #SEM * POR QUE DELETA TUDO!!!
        conexao.commit()
        excluiu = cursor.rowcount > 0
        cursor.close()
        conexao.close()
        return excluiu