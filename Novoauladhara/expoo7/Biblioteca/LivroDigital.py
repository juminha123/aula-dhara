from Livro import Livro


class LivroDigital(Livro):
    def __init__(self, titulo: str, autor: str, ano: int, tamanhoMb: float):
        super().__init__(titulo, autor, ano)
        self.tamanhoMb = tamanhoMb
        self._copiasEmprestadas = 0 
        
    def emprestar(self) -> str:
        self._copiasEmprestadas += 1
        return f'Cópia digital de ""{self.titulo} liberada para download'
    
    def devolver(self) -> str:
        if self._copiasEmprestadas > 0:
            self._copiasEmprestadas -= 1
            return f'Acesso ao e-book "{self.titulo}" encerrado.'
     
     #super().__str__() -> Execute da classe pai   
    def __str__(self):
        return f'{super().__str__()} [e-book, {self.tamanhoMb} MB]'