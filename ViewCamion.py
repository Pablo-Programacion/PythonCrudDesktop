from doctest import master
from tkinter import messagebox
import tkinter
from click import style
from tkinter import *
from tkinter import ttk
from ControladorCamion import *


class App:

    def __init__(self, master):
        try:
            self.ventana = master
            self.DibujarLabel()
            self.DibujarEntry()
            self.DibujarBoton()
            self.DibujarTabla()
        except:
            pass

    def DibujarLabel(self):
        try:
            self.lbl_nombre_general = Label(self.ventana, foreground="white",
                                            background="#314252", text="CAMIÓN", font=(20)).place(x=636, y=30)
            self.lbl_matricula = Label(self.ventana, foreground="white",
                                       background="#314252", text="Matricula", font=(8)).place(x=40, y=110)
            self.lbl_potencia = Label(self.ventana, foreground="white",
                                      background="#314252", text="Potencia", font=(8)).place(x=40, y=153)
            self.lbl_modelo = Label(self.ventana, foreground="white",
                                    background="#314252", text="Modelo", font=(8)).place(x=40, y=200)
            self.lbl_tipo = Label(self.ventana, foreground="white",
                                  background="#314252", text="Tipo", font=(8)).place(x=40, y=243)
        except:
            pass

    def DibujarEntry(self):
        try:
            self.matricula = StringVar()
            self.potencia = StringVar()
            self.modelo = StringVar()
            self.tipo = StringVar()
            self.txt_matricula = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.matricula).place(x=130, y=110)
            self.txt_potencia = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.potencia).place(x=130, y=153)
            self.txt_modelo = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.modelo).place(x=130, y=200)
            self.txt_tipo = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.tipo).place(x=130, y=243)
        except:
            pass

    def DibujarBoton(self):
        try:
            self.btn_guardar = Button(
                self.ventana, text="Insertar", relief="flat", background="#0051C8", cursor="hand1", foreground="white", command=lambda: self.insert()).place(x=1040, y=340, width=90)
            self.btn_cancelar = Button(
                self.ventana, text="Cerrar", relief="flat", background="red", cursor="hand1", foreground="white", command=lambda: self.cancelar()).place(x=1150, y=340, width=90)

        except:
            pass

    def DibujarTabla(self):
        try:
            self.lista = ttk.Treeview(self.ventana, columns=(
                1, 2, 3, 4), show="headings", height="8")
            # estilos de tabla
            estilo = ttk.Style()
            estilo.theme_use("clam")
            estilo.configure("Treeview.Heading", background="#0051C8",
                             relief="flat", foreground="black")

            self.lista.heading(1, text="Matricula")
            self.lista.heading(2, text="Potencia")
            self.lista.heading(3, text="Modelo")
            self.lista.heading(4, text="Tipo")

            self.lista.column(1, anchor=CENTER)
            self.lista.column(2, anchor=CENTER)
            self.lista.column(3, anchor=CENTER)
            self.lista.column(4, anchor=CENTER)

            self.lista.place(x=340, y=90, width=900)

            # Crear evento al hacer doble click en la tabla
            self.lista.bind("<Double 1>", self.obtenerFila)

            # Rellenar tabla
            d = ControlMySQL()
            elements = d.obtenerCamion()
            for i in elements:
                self.lista.insert('', 'end', values=i)
        except:
            pass

    def insert(self):
        try:
            int(self.potencia.get())
            if self.matricula.get() != "":
                arr = [self.matricula.get(), self.potencia.get(),
                       self.modelo.get(), self.tipo.get()]
                c = ControlMySQL()
                c.insertCamion(arr)
                self.matricula.set("")
                self.potencia.set("")
                self.modelo.set("")
                self.tipo.set("")
                self.LimpiarTabla()
                self.DibujarTabla()
            else:
                messagebox.showinfo(
                    title="Error", message="Necesitas insertar una matricula")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al insertar las variables")

    def LimpiarTabla(self):
        try:
            self.lista.delete(*self.lista.get_children())
        except:
            pass

    def obtenerFila(self, event):
        try:
            matricula = StringVar()
            potencia = StringVar()
            modelo = StringVar()
            tipo = StringVar()

            nombreFila = self.lista.identify_row(event.y)
            elemento = self.lista.item(self.lista.focus())
            m = elemento['values'][0]
            p = elemento['values'][1]
            mo = elemento['values'][2]
            t = elemento['values'][3]
            # ----------------------------------
            matricula.set(m)
            potencia.set(p)
            modelo.set(mo)
            tipo.set(t)
            pop = Toplevel(self.ventana)
            pop.title("Editar camion")
            # Centrar ventana en el medio
            ancho_ventana = 430
            alto_ventana = 330
            x_ventana = pop.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = pop.winfo_screenheight() // 2 - alto_ventana // 2
            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
                "+" + str(x_ventana) + "+" + str(y_ventana)
            pop.geometry(posicion)
            pop.resizable(0, 0)
            pop.config(background="#24363e")
            self.lbl_matricula = Label(pop, foreground="white",
                                       background="#24363e", text="Matricula", font=(8)).place(x=70, y=50)
            self.lbl_potencia = Label(pop, foreground="white",
                                      background="#24363e", text="Potencia", font=(8)).place(x=70, y=100)
            self.lbl_modelo = Label(pop, foreground="white",
                                    background="#24363e", text="Modelo", font=(8)).place(x=70, y=150)
            self.lbl_tipo = Label(pop, foreground="white",
                                  background="#24363e", text="Tipo", font=(8)).place(x=70, y=200)

            txt_m = Entry(pop, textvariable=matricula, font=(8)
                          ).place(x=160, y=50, width=180)
            txt_p = Entry(pop, textvariable=potencia, font=(8)
                          ).place(x=160, y=100, width=180)
            txt_mo = Entry(pop, textvariable=modelo, font=(8)
                           ).place(x=160, y=150, width=180)
            txt_t = Entry(pop, textvariable=tipo, font=(8)
                          ).place(x=160, y=200, width=180)
            # botones
            btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                                command=lambda: self.editarCamion(m, matricula.get(), potencia.get(), modelo.get(), tipo.get())).place(x=70, y=250, width=90)

            btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                                  command=lambda: self.eliminarCamion(matricula.get())).place(x=250, y=250, width=90)
        except:
            pass

    def editarCamion(self, m, matricula, potencia, modelo, tipo):
        try:
            int(potencia)
            if matricula != "":
                j = ControlMySQL()
                arr = [matricula, potencia, modelo, tipo]
                j.UpdateItem(arr, m)
                messagebox.showinfo(title="Actualización",
                                    message="Se ha actualizado la base  de datos")
                self.LimpiarTabla()
                self.DibujarTabla()
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar una matricula")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al editar las variables")

    def eliminarCamion(self, n):
        try:
            if n != "":
                j = ControlMySQL()
                j.eliminarCamion(n)
                messagebox.showinfo(title="Eliminar",
                                    message="Se ha actualizado la base  de datos")
                self.LimpiarTabla()
                self.DibujarTabla()
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar un codigo")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al eliminar")

    def cancelar(self):
        try:

            messagebox.showinfo(title="Base de Datos",
                                message="Se ha cerrado la base de datos")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al cerrar la base de datos")


def configCamion():
    root = tkinter.Toplevel()
    root.title("Crud Paqueteria")
    # Centrar ventana en el medio
    ancho_ventana = 1300
    alto_ventana = 400
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.resizable(0, 0)
    root.config(background="#314252")
    App(root)
    return root
