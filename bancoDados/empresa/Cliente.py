from produto.conexao import conectar


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
    def cadastrar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
            INSERT INTO clientes (nome, email, telefone)
            VALUES(%s, %s, %s)"""
        valores = (self.nome, self.email, self.telefone)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("cliente cadastrado com sucesso")
     
    @staticmethod
    def buscar_por_id(id_clientes):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT * FROM clientes WHERE id = %s"
        cursor.execute(sql, (id_clientes,))
        cliente = cursor.fetchone()
        cursor.close()
        conexao.close()
        return cliente
        
        