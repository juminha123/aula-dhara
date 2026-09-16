class Livro:
    def __init__(self, titulo:str, autor:str, quant: int):
        self.titulo = titulo
        self.autor = autor
        self.quant = quant
        self.emprestado = False
        
    
    
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print("livro emprestado com sucesso")
        else:
            print(" livro ja esta emprestado")
            
    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print("livro devolvido")
        else:
            print("disponivel")