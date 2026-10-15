class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo #encapsulamento
    def mostrardados(self):
        print("saldo:", self._saldo)
        print("saldo:", self.titular)