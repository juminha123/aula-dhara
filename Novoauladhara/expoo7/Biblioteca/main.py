from Biblioteca import Biblioteca
from Livro import Livro
from LivroDigital import LivroDigital


def menu():
    print("--------- MENU -----------")
    print(" 1 - cadastrar livro físico")
    print(" 2- cadastar e-book")
    print(" 3- listar livros disponiveis")
    print(" 4 - Emprestar livro")
    print(" 5 -  Devolver livro")
    return("escolha uma opção: ")
# na função: cadastrarlivrofosico, recebemos a biblio como parametro para receber um objeto da classe biblioteca
def cadastrarLivroFisico(biblioteca: Biblioteca):
    titulo = input("título do livro:")
    autor = input("autor:")
    ano = int(input("ano:"))
    
    livro = Livro(titulo, autor, ano)
    biblioteca.adicionarLivro(livro)
    
def cadastrarEbook(biblioteca: Biblioteca):
    titulo = input("título do livro:")
    autor = input("autor:")
    ano = int(input("ano:"))
    tamanhoMb = float(input("tamanho: "))
    
    ebook = LivroDigital(titulo, autor, ano,tamanhoMb)
    biblioteca.adicionarLivro(ebook)
    
def emprestarLivro(biblioteca: Biblioteca):
    titulo = input("título do livro q deseja pegar:")
    livro = biblioteca.buscarTitulo(titulo)
    if livro is None:
        print("Livro não encontrado  na biblioteca")
        return #encerra a função imediatamente
    
    print(livro.emprestar())
    
def devolverLivro(biblioteca: Biblioteca):
    titulo = input("título do livro que deseja devolver: ")
    Livro = biblioteca.buscarTitulo(titulo)
    if Livro is None:
        print("Livro não encontrado  na biblioteca")
        return
    print(Livro.devolver(titulo))
    
def main():
    nomeBiblioteca = input("digite o nome da biblioteca: ")
    #objeto do classe biblio
    biblioteca = Biblioteca(nomeBiblioteca)
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrarLivroFisico(biblioteca)
        elif opcao == "2":
            cadastrarEbook(biblioteca)
        elif opcao == "3":
            biblioteca.listarDisponiveis()
        elif opcao == "4":
            emprestarLivro(biblioteca)
        elif opcao == "5":
            devolverLivro(biblioteca)
        elif opcao == "0":
            print("encerrando o programa...")
            break
        else:
            print("invalido")
#inicio do programa
if __name__ == "__main__":
    main()