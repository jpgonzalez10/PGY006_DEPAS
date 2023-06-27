from colorama import Style
import numpy
import os
import msvcrt

depas=numpy.empty([2,10,4], object)

def dibujarEdificio():
    print("    A   B   C   D")
    for x in range(10):     #Filas
        if 10-x<10:
            print(f"0{10-x}", end="|")
        else:
            print(10-x, end="|")
        for y in range(4):  #Columnas
            if depas[0,x,y]==None:
                print(f"🟩",end=" |")
            else:
                print(f"🟥",end=" |")
        print(" ")
           
dibujarEdificio()

def limpiarPantalla():
    pass

def printr(texto):
    pass

def compraDepa(piso,columna):
    pass

def pagar(costo,pagar):
    pass

def buscarDueno():
    pass