from produto.conexao import conectar


class Aluno:
    def __init__(self,nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def cadastrar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO alunos(nome, idade, curso) VALUES (%s, %s, %s)"
        valores = (self.nome, self.idade, self.curso)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("aluno cadastrado com sucesso!")
        
    @staticmethod   
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
       
        for aluno in alunos:
           print(
               f"ID {aluno[0]} |"
               f"nome {aluno[1]} |"
               f"idade {aluno[2]} |"
               f"curso {aluno[3]} |"
           )
        cursor.close()
        conexao.close()