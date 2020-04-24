
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
    boton2 = Button(root, text="Aceptar", command = lambda: Asientos(campo2.get()), font= ("Verdana",15),background="white").place(x=0,y=height/3 + 70)
    pregunta3 = "¿Cuántas personas van en el carro?"
    etiqueta3 = Label(text=pregunta3, font= ("Verdana",15),background="white").place(x=0, y=height/2)
    campo3 = Entry(root)
    campo3.insert(0, "")
    campo3.place(x=0,y=height/2 + 40)
    boton3 = Button(root, text="Aceptar",command = lambda: Disponibilidad(campo3.get()), font= ("Verdana",15),background="white").place(x=0,y=height/2 + 70)
    subprocess.call("./a.exe")

def Ubicacion(entry):
    if entry == "Universidades":
        print("Sigue el camino")
        #Funcion del grafo de c++
    elif entry== "A casa":
        print("Sigue el camino devuelta")

def Asientos(entry): #Cuantos asientos hay
    print(entry)
    archivo = open("Asientos.txt", "w")
    archivo.write(entry)
    archivo.close()

def Disponibilidad(entry):
    print(entry)
    archivo2 = open("Dispo.txt", "w")
    archivo2.write(entry)
    archivo2.close()

def limpiar():
    root.destroy()


Grafica()
root.mainloop()
