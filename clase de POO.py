






class Pajaro:
    alas=True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")


    def volar(self,metros):
        print(f"el ave a volado {metros}")
        self.piar()
        
    def pintarP(self):
        self.color = "negro"
        print(f"ahora el color del pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} de huevos")



mi_pajaro = Pajaro("rojo", "tucan")

print(mi_pajaro.color, mi_pajaro.especie)
print(mi_pajaro.volar(50))
print(mi_pajaro.pintarP())
print(mi_pajaro.poner_huevos(5))
print(Pajaro.poner_huevos(40))

class Personaje:
    def __init__(self,cantidad_Flechas):
        self.cantidad_Flechas = cantidad_Flechas

    def lanzar_Flechas(self):
        self.cantidad_Flechas-=1

arquero = Personaje(5)
arquero.lanzar_Flechas()
print(arquero.cantidad_Flechas)
