from conexao import conectar


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def cadastrar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
            INSERT INTO funcionarios (nome, cargo, salario)
            VALUES(%s, %s, %s)"""
        valores = (self.nome, self.cargo, self.salario)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("funcionario cadastrado com sucesso")
        
    @staticmethod    
    def alterar(nome, cargo, salario, idFuncionario):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
            UPDATE funcionarios
            SET nome = %s, cargo = %s, salario = %s
            WHERE id = %s
        """
        valores = (nome, cargo, salario, idFuncionario)
        cursor.execute(sql, valores)
        conexao.commit()
        alterou = cursor.rowcount > 0
        cursor.close()
        conexao.close
        return alterou