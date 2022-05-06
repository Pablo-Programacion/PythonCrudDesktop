from doctest import master
from tkinter import messagebox
import tkinter
from click import style
from tkinter import *
from tkinter import ttk
from ControladorProvincias import *


class App:
    root = 0

    def __init__(self, master):
        try:
            self.ventana = master
            self.DibujarLabel()
            self.DibujarEntry()
            self.DibujarBoton()
            self.DibujarTabla("")
        except:
            pass

    def DibujarLabel(self):
        try:
            self.lbl_nombre_general = Label(self.ventana, foreground="white",
                                            background="#314252", text="PROVINCIA", font=(20)).place(x=470, y=30)
            self.lbl_codigo = Label(self.ventana, foreground="white",
                                    background="#314252", text="Codigo Postal", font=(8)).place(x=20, y=140)
            self.lbl_name = Label(self.ventana, foreground="white",
                                  background="#314252", text="Nombre", font=(8)).place(x=60, y=190)
        except:
            pass

    def DibujarEntry(self):
        try:
            self.nombre = StringVar()
            self.codigo = StringVar()
            self.buscar = StringVar()

            self.txt_codigo = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.codigo).place(x=140, y=140)
            self.txt_nombre = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.nombre).place(x=140, y=190)
            # Agregación de buscar
            self.txt_buscar = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.buscar).place(x=60, y=340)

        except:
            messagebox.showinfo(title="Error",
                                message="Error en los entrys",parent=configProvincias())

    def DibujarBoton(self):
        try:
            self.btn_guardar = Button(
                self.ventana, text="Insertar", relief="flat", background="#0051C8", cursor="hand1", foreground="white", command=lambda: self.insert()).place(x=750, y=340, width=90)
            self.btn_cancelar = Button(
                self.ventana, text="Cerrar", relief="flat", background="red", cursor="hand1", foreground="white", command=lambda: self.cancelar()).place(x=850, y=340, width=90)
            self.btn_buscar = Button(
                self.ventana, text="Filtrado Código", relief="flat", background="Green", cursor="hand1", foreground="white", command=lambda: self.buscarProvincia(self.buscar.get())).place(x=260, y=339, width=100)

        except:
            pass

    def buscarProvincia(self, ref):
        self.LimpiarTabla()
        self.DibujarTabla(ref)

    def DibujarTabla(self, ref):
        try:
            self.lista = ttk.Treeview(self.ventana, columns=(
                1, 2), show="headings", height="8")
            # estilos de tabla
            estilo = ttk.Style()
            estilo.theme_use("clam")
            estilo.configure("Treeview.Heading", background="#0051C8",
                             relief="flat", foreground="black")

            self.lista.heading(1, text="Codigo")
            self.lista.heading(2, text="Nombre")
            self.lista.column(1, anchor=CENTER)
            self.lista.column(2, anchor=CENTER)
            self.lista.place(x=340, y=90, width=600)

            # Crear evento al hacer doble click en la tabla
            self.lista.bind("<Double 1>", self.obtenerFila)
            ''' He pensado ya que el filtrado no serviria mucho en este caso en hacer un id principal y que codigo
            postal fuera opcional y añadir comunidad autonoma y poder hacer el filtrado de eso '''
            if ref == "":
                # Rellenar tabla
                d = ControlMySQL()
                elements = d.obtenerProvincias()
                for i in elements:
                    self.lista.insert('', 'end', values=i)
            else:
                # Rellenar tabla
                d = Data()
                elements = d.buscarFiltroCodigo(ref)
                for i in elements:
                    self.lista.insert('', 'end', values=i)
        except:
            messagebox.showinfo(
                title="Error", message="error",parent=configProvincias())

    def insert(self):
        try:
            int(self.codigo.get())
            if self.codigo.get() != "":
                arr = [self.codigo.get(), self.nombre.get()]
                c = ControlMySQL()
                c.insertProvincia(arr)
                self.codigo.set("")
                self.nombre.set("")
                self.LimpiarTabla()
                self.DibujarTabla("")
            else:
                messagebox.showinfo(
                    title="Error", message="Necesitas insertar un codigo",parent=configProvincias())
        except:
            messagebox.showinfo(title="Error",
                                message="Error al insertar",parent=configProvincias())

    def LimpiarTabla(self):
        try:
            self.lista.delete(*self.lista.get_children())
        except:
            pass

    def obtenerFila(self, event):
        try:
            cod = StringVar()
            nom = StringVar()
            nombreFila = self.lista.identify_row(event.y)
            elemento = self.lista.item(self.lista.focus())
            c = elemento['values'][0]
            n = elemento['values'][1]
            cod.set(c)
            nom.set(n)
            pop = Toplevel(self.ventana)
            pop.title("Editar provincia")
            # Centrar ventana en el medio
            ancho_ventana = 400
            alto_ventana = 200
            x_ventana = pop.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = pop.winfo_screenheight() // 2 - alto_ventana // 2
            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
                "+" + str(x_ventana) + "+" + str(y_ventana)
            pop.geometry(posicion)
            pop.resizable(0, 0)
            pop.config(background="#24363e")
            self.lbl_codigo = Label(pop, foreground="white",
                                    background="#24363e", text="Codigo", font=(8)).place(x=70, y=50)
            self.lbl_name = Label(pop, foreground="white",
                                  background="#24363e", text="Nombre", font=(8)).place(x=70, y=100)

            txt_c = Entry(pop, textvariable=cod, font=(8)
                          ).place(x=160, y=50, width=180)
            txt_n = Entry(pop, textvariable=nom, font=(8)
                          ).place(x=160, y=100, width=180)
            # botones
            btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                                command=lambda: self.editar(c, cod.get(), nom.get())).place(x=180, y=160, width=90)

            btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                                  command=lambda: self.eliminarProvincia(cod.get())).place(x=290, y=160, width=90)
        except:
            pass

    def editar(self, c, codigo, nombre):
        try:
            int(codigo)
            if codigo != "":
                j = ControlMySQL()
                arr = [codigo, nombre]
                j.UpdateItem(arr, c)
                messagebox.showinfo(title="Actualización",
                                    message="Se ha actualizado la base  de datos",parent=configProvincias())
                self.LimpiarTabla()
                self.DibujarTabla("")
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar un codigo",parent=configProvincias())
        except:
            messagebox.showinfo(title="Error",
                                message="Error al editar",parent=configProvincias())

    def eliminarProvincia(self, n):
        try:
            int(n)
            if n != "":
                j = ControlMySQL()
                j.eliminarProvincia(n)
                messagebox.showinfo(title="Eliminar",
                                    message="Se ha actualizado la base  de datos",parent=configProvincias())
                self.LimpiarTabla()
                self.DibujarTabla("")
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar un codigo",parent=configProvincias())
        except:
            messagebox.showinfo(title="Error",
                                message="Error al eliminar",parent=configProvincias())

    def cancelar(self):
        try:
            messagebox.showinfo(title="Base de Datos",
                                message="Se ha cerrado la base de datos",parent=configProvincias())
        except:
            messagebox.showinfo(title="Error",
                                message="Error al cerrar la base de datos",parent=configProvincias())


def configProvincias():
    root = tkinter.Toplevel()
    root.title("Crud Paqueteria")
    # Centrar ventana en el medio
    ancho_ventana = 1000
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
