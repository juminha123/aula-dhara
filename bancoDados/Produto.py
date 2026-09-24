from conexao import conectar


class Produto:
    def __init__(self, nome,preco):
        self.nome = nome
        self.preco = preco
        
    def cadastrar(self):
        #chamar a conexão com o banco pela função
        conexao = conectar()
        # o cursor é utilizado para executar comando sql
        cursor = conexao.cursor()
        #criar o comando SQL para inserir um produto
        #"%s" valor que o usuario insere no programa e cai para o banco
        sql = """
            INSERT INTO produtos(nome, preco)
            VALUES(%s, %s)"""
        valores = (self.nome, self.preco)
        #executamos o comando SQL
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("produto cadastrado com sucesso")
        
    @staticmethod   
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        produtos = cursor.fetchall() #lista para banco de dados
        
        for produto in produtos:
            print(
                f"id {produto[0]}|"
                f"nome {produto[2]}|"
                f"preço {produto[1]}|"
            )
        cursor.close()
        conexao.close()