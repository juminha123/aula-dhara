

from Biblioteca import Biblioteca
from Livro import Livro
from Usuario import Usuario


biblioteca = Biblioteca()

livros2 = Livro(
    "Capitães da Areia",
    "Jorge Amado"
)
livros1 = Livro(
    "hora da estrela",
    "Clarisse Lispector"
)

usuario = Usuario("João")

biblioteca.adicionarLivro(livros1)
biblioteca.adicionarLivro(livros2)
biblioteca.adicionarUsuario(usuario)

biblioteca.listarLivros()


