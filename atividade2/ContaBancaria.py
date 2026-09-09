class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def apresentar(self):
        print(f"titular: {self.titular}")    
        print(f"saldo atual: {self.saldo}")
    
    def adicionarSaldo(self, valor):
        valor = int(input("Quanto deseja adicionar: "))
        self.saldo = self.saldo + valor
        print("saldo atual: ", self.saldo)
        
    def retirarSaldo(self, ValorparaRetirar):
        ValorparaRetirar = int(input("Quanto deseja retirar: "))
        
        if self.saldo >= ValorparaRetirar:
           self.saldo = self.saldo - ValorparaRetirar
           print("Ação efetuada com sucesso! seu valor atual é de", self.saldo)
        else:
            print("valor insuficiente!")
            
          
