
class Carr:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.arrancado=False
    
    def presentacion(self):
        print(self.marca)
        print(self.modelo)
        print(self.arrancado)
    
    def arrancar(self):
        self.arrancado=True
        print("El coche", self.marca, self.modelo, "se ha arrancado")

diablo=Carr("Lamborgini",2022)
diablo.presentacion()
diablo.arrancar()

tesla=Carr("tesla","tesla model 3")
tesla.presentacion()
tesla.arrancar()