import tkinter
from tkinter import Label, messagebox
from tkinter.font import BOLD
from ViewPaquete import configPaquete

from ViewProvincias import *
from ControladorProvincias import *
from ViewCamionero import *
from ViewCamion import *
from PIL import Image, ImageTk
from datetime import date, time, datetime


# Crea una ventana con unos pocos botones.
class general12:
    general12 = 0

    def __init__(self, general12):
        '''  Contructor'''
    # Provincias

    def generate_new_window2():
        window = configProvincias()

    # Camión

    def generate_new_window():
        window = configCamion()

    # Paquete

    def generate_new_window3():
        window3 = configPaquete()

    # Camionero

    def generate_new_window4():
        window = configCamionero()

    def exitProgram(self, root):
        root.destroy()

    root = tkinter.Tk()

    root.lbl_nombre_general = Label(root, foreground="white",
                                    background="#314252", text="", font=(20), width=35, height=800).place(x=0, y=0)
    textinicial = """ 
    A HispaTrans, Software de Gestión orientado a Empresas de Paquetería para Administrar de Forma Óptima y Fácil el Flujo de envío de Paquetes, Control de Flota de Vehículo…

Esta herramienta nos permite llevar un control completo y detallado de su Empresa, tendrá acceso a herramientas especiales para tareas específicas, como lo son:

- Registrar envíos (Paquetes).
- Registrar nuevos trabajadores (Camioneros).
- Controlar la flota de Vehículos de Transporte (Camiones).
- Ver que Vehículos de Transporte, tiene asignado cada Trabajador (Camionero).
- Búsqueda Avanzada de Envíos por Camionero (DNI) o Fecha de Envio (Paquete).
- Editar y Eliminar cualquier tipo de Registro."""
    img  = Image.open("foto.jpg") 
    img = img.resize((500, 500), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(img)
    lab=Label(image=photo).place(x=500,y=340)

    root.lbl_nombre_general3 = Label(root, foreground="black",
                                     background="white", text=date.today(), font=("Arial", 10)).place(x=310, y=0)

    root.lbl_nombre_general3 = Label(root, foreground="black",
                                     background="white", text="Bienvenido", font=("Arial", 14)).place(x=760, y=170)
    root.lbl_nombre_general3 = Label(root, foreground="black",
                                     background="white", text=textinicial, font=("Arial", 9)).place(x=320, y=200)
    root.lbl_nombre_general2 = Label(root, foreground="white",
                                     background="#314252", text="", font=(20), width=1300, height=7).place(x=0, y=22)
    root.lbl_nombre_general3 = Label(root, foreground="white",
                                     background="#314252", text="HispaTrans", font=("Arial", 18)).place(x=102, y=20)
    root.lbl_nombre_general4 = Label(root, foreground="white",
                                     background="#314252", text="Almacenes", font=("Arial", 12)).place(x=120, y=55)

    spawn_window_button = tkinter.Button(root,
                                         text="Flota de Vehículos",
                                         command=generate_new_window, relief="flat", font=(
                                             'Arial', 12), foreground="white",
                                         background="#314252").place(x=100, y=380)

    spawn_window_button2 = tkinter.Button(root,
                                          text="Provincias",
                                          command=generate_new_window2, relief="flat", font=(
                                              'Arial', 12), foreground="white",
                                          background="#314252").place(x=125, y=175)

    spawn_window_button2 = tkinter.Button(root,
                                          text="Provincias",
                                          command=generate_new_window2, relief="flat", font=(
                                              'Arial', 12), foreground="white",
                                          background="#314252").place(x=125, y=175)

    spawn_window_button3 = tkinter.Button(root,
                                          text="Envios",
                                          command=generate_new_window3, relief="flat", font=(
                                              'Arial', 12), foreground="white",
                                          background="#314252").place(x=133, y=240)

    spawn_window_button4 = tkinter.Button(root,
                                          text="Personal",
                                          command=generate_new_window4, relief="flat", font=(
                                              'Arial', 12), foreground="white",
                                          background="#314252").place(x=127, y=310)

    ancho_ventana = 1300
    alto_ventana = 800
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.resizable(0, 0)
    root.mainloop()
