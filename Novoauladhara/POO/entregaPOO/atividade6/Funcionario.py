class Funcionario:
    def __init__(self, nome,cargo,salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def aumento(self):
        aumento = int(input("informe o valor do aumento"))
        self.salario += self.salario * aumento /100
        
    def exibirdados(self):
        print(f"funcionario: {self.nome}") 
        print(f"cargo: {self.cargo}") 
        print(f"saldo atual: {self.salario}")