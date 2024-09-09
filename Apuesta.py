class Apuesta:
    
    def __init__(self):
        self.fichas = 0
    
    def __repr__(self):
        return  f"Apuesta: {self.fichas} ficha/s"
    
    def ponerFicha(self, poner=1):
        self.fichas = self.fichas + poner
    
    def tomarFicha(self, tomar = 1):
        self.tomar = tomar
        
        if self.fichas < self.tomar:
            raise ValueError("La cantidad de fichas apostadas no son suficientes")
        else:
            self.fichas = self.fichas - self.tomar

    def tomarTodas(self):
        print(f"toma {self.fichas} ficha/s")
        self.fichas = 0

    def tieneFicha(self, cuantas= 1):
        if self.fichas == cuantas:
            return True
        
    def estaVacia(self):
        if self.fichas == 0:
            return True
        