class Personaje:
    nombre="Katheringo"
    fuerza=0
    inteligencia=0
    defensa=0
    vida=0
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
        
    
personaje1=Personaje()

print("El nombre de mi personaje es ",personaje1.nombre)
print("la fuerza de mi personaje es ",personaje1.fuerza)

