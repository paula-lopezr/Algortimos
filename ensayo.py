#https://es.stackoverflow.com/questions/9069/c%C3%B3mo-llamar-a-c%C3%B3digo-c-desde-python
# import subprocess
# from tkinter import *
# cimport carro.cpp
# from distutils.core import setup, Extension
# from Cython.Build import cythonize
# cdef extern from "carro.hpp":
#     void setAs(int dispo)

from tkinter import *
import subprocess
import os

width = 1024
height=1024
root = Frame(height=height, width = width,background="lightblue")
root.pack(padx = 0,pady = 0)
contador = 0
c_glob = 0
Titulo = Label(text="CARPOOLING", font =("Verdana", 40), background = "white").place(x=0, y = 40)


def Grafica():
    pregunta = "¿Hacia dónde se dirige?"
    etiqueta = Label(text=pregunta, font= ("Verdana",15),background="white").place(x=0, y=height/6)
    campo = Entry(root)
    campo.insert(0, "")
    campo.place(x=0, y=(height/6) + 40)
    boton = Button(root, text="Aceptar", command = lambda: Ubicacion(campo.get()), font= ("Verdana",15),background="white").place(x=0,y=(height/6) + 70)
    pregunta2 = "¿Cuantos asientos tiene su carro?"
    etiqueta2 = Label(text=pregunta2, font = ("Verdana", 15), background ="white").place(x=0, y=height/3)
    campo2 = Entry(root)
    campo2.insert(0, "")
    campo2.place(x=0,y=height/3 + 40)
    boton2 = Button(root, text="Aceptar", command = lambda: Asientos(campo.get()), font= ("Verdana",15),background="white").place(x=0,y=height/3 + 70)
    pregunta3 = "¿Cuántas personas van en el carro?"
    etiqueta3 = Label(text=pregunta3, font= ("Verdana",15),background="white").place(x=0, y=height/2)
    campo3 = Entry(root)
    campo3.insert(0, "")
    campo3.place(x=0,y=height/2 + 40)
    boton3 = Button(root, text="Aceptar",command = lambda: Disponibilidad(campo.get()), font= ("Verdana",15),background="white").place(x=0,y=height/2 + 70)
    subprocess.call("./a.exe")

def Ubicacion(entry):
    if entry == "Universidades":
        print("Sigue el camino")
        #Funcion del grafo de c++
    elif entry== "A casa":
        print("Sigue el camino devuelta")

def Asientos(entry): #Cuantos asientos hay
    f = open("Asientos.txt", "w")
    f.write(str(entry))
    f.close()

def Disponibilidad(entry):
    f1 = open("Dispo.txt", "w")
    f1.write(str(entry))
    f1.close()

# def Disponibilidad(entry):
#     file2 = open("dispo.txt", "w")
#     file2.write(str(entry) + os.linesep)
#     file2.close()
# #    etiqueta3 = Label(text="Ok", font = ("Verdana", 15), background ="white").place(x=0, y=height/2)
#     subprocess.call("./a.exe")
#     file2 = open("Asientos.txt", "r")
#     as = file2.read()
#     # Ent = int(entry)
#     # carro.setAs(Ent)
#     # return carro.getAs()

def limpiar():
    root.destroy()


Grafica()
root.mainloop()
