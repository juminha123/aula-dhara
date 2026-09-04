#herdar da classe animal
from Animal import Animal

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")