import tkinter
from tkinter import Label, messagebox
from tkinter.font import BOLD
import ViewProvincias
import ViewCamion


class general12:
    def __init__(self, master):
        a = 9
    # Provincias

    def generate_new_window2():
        window = ViewProvincias.configProvincias()
    # Camión

    def generate_new_window():
        window2 = ViewCamion.configCamion()

    def generate_new_window3():
        window3 = 0

    def generate_new_window4():
        window3 = 0

    root = tkinter.Tk()

    root.lbl_nombre_general = Label(root, foreground="white",
                                    background="#314252", text="", font=(20), width=35, height=800).place(x=0, y=0)
    root.lbl_nombre_general2 = Label(root, foreground="white",
                                     background="#314252", text="", font=(20), width=1300, height=7).place(x=0, y=15)
    root.lbl_nombre_general3 = Label(root, foreground="white",
                                     background="#314252", text="HispaTrans",font=("Arial", 18)).place(x=102, y=20)
    root.lbl_nombre_general4 = Label(root, foreground="white",
                                     background="#314252", text="Almacenes",font=("Arial", 12)).place(x=120, y=55)
    
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

    spawn_window_button4 = tkinter.Button(root,
                                          text="Iniciar Sesión",
                                          command=generate_new_window4, relief="flat",font=("Arial", 12), foreground="white",
                                          background="#314252").place(x=110, y=750)
    root.overrideredirect(True)
    ancho_ventana = 1300
    alto_ventana = 800
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.resizable(0, 0)
  
    root.mainloop()
