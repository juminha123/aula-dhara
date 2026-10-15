class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
    
    def adicionarLivro(self, livro):
        self.livros.append(livro)
    def adicionarUsuario(self,usuario):
        self.usuarios.append(usuario)
    def listarLivros(self):
        print("LIVROS DA BIBLIOTECA")
        for livro in self.livros:
            livro.mostrar()
            print("---------------")