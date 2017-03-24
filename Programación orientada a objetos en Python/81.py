class Persona:
    nBrazos=0
    nPiernas=0
    cabello=True
    cCabello="Defecto"
    hambre=0

    def __init__(self):
        self.nBrazos=2
        self.nPiernas=2

    def dormir():
        pass
    def comer(self):
        self.hambre=0

class Hombre(Persona):
    nombre="Defecto"
    sexo="M"
    def cambiarNombre(self,nombre):
        self.nombre=nombre

class Mujer(Persona):
    nombre="Defecto"
    sexo="F"

jose=Hombre()
jose.comer()