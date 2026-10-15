class Livro:
    def __init__(self,titulo, autor):
     self.titulo = titulo
     self.autor = autor
     self.disponivel = True
     
    def mostrar(self):
        print(f"Título:{self.titulo}")
        print(f"Autor:{self.autor}")
        
        if self.disponivel:
            print("status: disponivel")
        else:
            print("indisponivel")