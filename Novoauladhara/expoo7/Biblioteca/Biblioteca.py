from Livro import Livro


class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.acervo = []
       
    def adicionarLivro(self, livro: Livro):
        self.acervo.append(livro)
        print(f"Adicionar ao acervo: {livro.titulo}")
       
    def listarDisponiveis(self):
        print(f"----------Livros disponiveis em {self.nome}----------")
        disponiveis = [livro for livro in self.acervo if livro.dispnivel]
        if not disponiveis:
            print("Nenhum livro isponivel no momento")
 
        for livro in disponiveis:
            print(f"- {livro}")
           
    def buscarTitulo(self, titulo: str):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        #none não encontrado
        return None