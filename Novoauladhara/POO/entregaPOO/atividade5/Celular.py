class Celular:
    def __init__(self,marca,modelo,bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False
        
    def ligar(self):
        if self.bateria > 0:
            self.ligado = True
            print("celular ligado")
            
        else:
            print("celular desligado")
            
    def desligar(self):
        self.ligado = False
        print("celular esta desligado")
        
    def ligacao(self):
        self.ligado = True
        if not self.ligado:
            print("Não é possivel fazer ligação")
        elif self.bateria <= 0:
            print("Não é possivel fazer ligação")
        else:
            self.bateria -= 10
            print("piririn piririn piririn alguém ligou pra mim!")
            print("bateria restante: ", self.bateria)
    
                
        
    