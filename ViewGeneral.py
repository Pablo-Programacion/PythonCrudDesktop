import tkinter
from tkinter import messagebox
import ViewProvincias
import ViewCamion


def generate_new_window2():
    window = ViewProvincias.configProvincias()


def generate_new_window():
    window2 = ViewCamion.configCamion()


root = tkinter.Tk()


spawn_window_button = tkinter.Button(root,
                                     text="Camión",
                                     command=generate_new_window, relief="flat").place(x=0, y=70)

spawn_window_button2 = tkinter.Button(root,
                                      text="Provincias",
                                      command=generate_new_window2, relief="flat").place(x=0, y=30)


ancho_ventana = 1000
alto_ventana = 400
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root.resizable(0, 0)
root.mainloop()
