class Livro:
    def __init__(self, titulo:str, autor:str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._esprestado = False
        
    @property #sem @property = livro.disponivel()
    #com @property = livro.disponivel
    
    def disponivel(self) -> bool: #transforma o método a abaixo em algo que podemos acessar como se fosse um atributo ou variavel
        return not self._esprestado
    def empresrtarO(self) -> str:
        if self._emprestado:
            return f'o livro"{self.titulo}" ja esta emprestado'
        self._mprestado = True
        return f'vc pegou emprestado: "{self.titulo}"'
    
    #metodo devolver
    def devolver(self) -> str:
        #false significa que o livro não esta emprestado. portanto livro está disponivel
        self._emprestado = False
        return f'livro "{self.titulo}" devolvido. obrigada'
    
    def __str__(self) -> str:
        status = "disponivel" if self.disponivel else "emprestado"
        return f'"{self.titulo}" ({self.ano}) de {self.autor} - {status}'