from personaje import Personaje
import random


nombre=input(""" 
             !!!Bienvenido a Gran Fantasia!!!
             por favor ingresa el  nombre de tu personaje: """)

p=Personaje(nombre)

print(p.estado)

print("¡¡¡oh no!!! , Ha aparecido un orco!!!")

o=Personaje("Orco")

probabilidad_de_ganar=p.mostrar_probabilidad(o)

opcion_orco=Personaje.mostrar_dialogo_y_opciones(probabilidad_de_ganar)

while opcion_orco==1:
    resultado="G" if random.uniform(0,1)<probabilidad_de_ganar else "P"
    if resultado=="G":
            print("""
                Le has ganado al orco, felicidades!!
                Has ganado 50 de experiencia
                """)
            p.estado=50
            o.estado=-30
            print(p.estado)
            print(o.estado)
    else:
            print("""
                El orco te ha derrotado
                has perdido 30 de experiencia
                """)
            p.estado=-30
            o.estado=50   
            print(p.estado)
            print(o.estado)
    probabilidad_de_ganar=p.mostrar_probabilidad(o)
    opcion_orco=Personaje.mostrar_dialogo_y_opciones(probabilidad_de_ganar)
print("Has huido del orco")