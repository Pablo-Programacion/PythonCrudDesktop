from ast import Lambda
from msilib.schema import Control
from tkinter import messagebox
from turtle import heading

from click import style
from matplotlib.pyplot import text
from ModeloMySQL import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ControladorMySQL import *


class App:
    def __init__(self, master):
        self.ventana = master
        self.DibujarLabel()
        self.DibujarEntry()
        self.DibujarBoton()
        self.DibujarTabla()

    def DibujarLabel(self):
        self.lbl_codigo = Label(self.ventana, foreground="white",
                                background="#314252", text="Codigo", font=(8)).place(x=60, y=140)
        self.lbl_name = Label(self.ventana, foreground="white",
                              background="#314252", text="Nombre", font=(8)).place(x=60, y=190)

    def DibujarEntry(self):
        self.nombre = StringVar()
        self.codigo = StringVar()
        self.txt_codigo = Entry(self.ventana, font=(
            'Arial', 12), textvariable=self.codigo).place(x=140, y=140)
        self.txt_nombre = Entry(self.ventana, font=(
            'Arial', 12), textvariable=self.nombre).place(x=140, y=190)

    def DibujarBoton(self):
        self.btn_guardar = Button(
            self.ventana, text="Insertar", relief="flat", background="#0051C8", cursor="hand1", foreground="white", command=lambda: self.insert()).place(x=750, y=340, width=90)
        self.btn_cancelar = Button(
            self.ventana, text="Cancelar", relief="flat", background="red", cursor="hand1", foreground="white").place(x=850, y=340, width=90)

    def DibujarTabla(self):
        self.lista = ttk.Treeview(self.ventana, columns=(
            1, 2), show="headings", height="8")
        # estilos de tabla
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview.Heading", background="#0051C8",
                         relief="flat", foreground="white")
        self.lista.heading(1, text="Codigo")
        self.lista.heading(2, text="Nombre")
        self.lista.column(2, anchor=CENTER)
        self.lista.place(x=340, y=90, width=600)

        # Crear evento al hacer doble click en la tabla
        self.lista.bind("<Double 1>", self.obtenerFila)

        # Rellenar tabla
        d = Data()
        elements = d.obtenerProvincias()
        for i in elements:
            self.lista.insert('', 'end', values=i)

    def insert(self):
        arr = [self.codigo.get(), self.nombre.get()]
        c = ControlMySQL()
        c.insertProvincia(arr)
        self.codigo.set("")
        self.nombre.set("")
        self.LimpiarTabla()
        self.DibujarTabla()

    def LimpiarTabla(self):
        self.lista.delete(*self.lista.get_children())

    def obtenerFila(self, event):
        cod = StringVar()
        nom = StringVar()
        nombreFila = self.lista.identify_row(event.y)
        elemento = self.lista.item(self.lista.focus())
        c = elemento['values'][0]
        n = elemento['values'][1]
        cod.set(c)
        nom.set(n)
        pop = Toplevel(self.ventana)
        pop.geometry("400x200")
        txt_c = Entry(pop, textvariable=cod).place(x=40, y=50)
        txt_n = Entry(pop, textvariable=nom).place(x=40, y=100)
        # botones
        btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                            command=lambda: self.editar(c, cod.get, nom.get)).place(x=180, y=160, width=90)

        btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                              command=lambda: self.eliminar(cod.get)).place(x=290, y=160, width=90)

    def editar(self, c, codigo, nombre):
        messagebox.showinfo(title="Actualización", message=c )
        d = Data()
        arr = [codigo, nombre]
        d.UpdateItem(arr, c)
        messagebox.showinfo(title="Actualización",
                            message="Se ha actualizado la base  de datos")
        self.LimpiarTabla()
        self.DibujarTabla()


root = Tk()
root.title("Crud Paqueteria")
root.geometry("1000x400")
root.config(background="#314252")
aplicacion = App(root)
root.mainloop()
