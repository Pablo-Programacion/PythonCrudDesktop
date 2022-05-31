from doctest import master
from tkinter import messagebox
import tkinter
from click import style
from tkinter import *
from tkinter import ttk
from ControladorProvincias import *


class App:
    root = 0

    """
    Crea una ventana con una etiqueta, una entrada, un botón y una tabla.
    
    @param master La ventana principal
    """

    def __init__(self, master):
        try:
            master.attributes("-topmost", False)
            self.ventana = master
            self.DibujarLabel(master)
            self.DibujarEntry(master)
            self.DibujarBoton(master)
            self.DibujarTabla("")
        except:
            messagebox.showinfo(title="Error",
                                message="No se pudieron dibujar los contains", parent=master)

    """
    Crea una etiqueta con el texto "PROVINCIA" y la ubica en x=470, y=30
    
    @param master La ventana principal.
    """

    def DibujarLabel(self, master):
        try:
            self.lbl_nombre_general = Label(self.ventana, foreground="white",
                                            background="#202931", text="PROVINCIA", font=(20)).place(x=470, y=30)
            self.lbl_codigo = Label(self.ventana, foreground="white",
                                    background="#202931", text="Codigo Postal", font=(8)).place(x=20, y=140)
            self.lbl_name = Label(self.ventana, foreground="white",
                                  background="#202931", text="Nombre", font=(8)).place(x=60, y=190)
        except:
            messagebox.showinfo(title="Error",
                                message="No se pudieron dibujar los labels", parent=master)

    """
    Crea tres variables, luego crea tres widgets de entrada y los coloca en la ventana
    
    @param master La ventana principal.
    """

    def DibujarEntry(self, master):
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
                                message="Error en los entrys", parent=master)

    """
    Cierra la ventana.
    
    @param window La ventana en la que se encuentra actualmente el usuario.
    """

    def exitProgram(self, window):
        window.destroy()
        window.update()

    """
    Crea tres botones, uno de los cuales tiene una función lambda como comando.
    
    @param master La ventana principal
    """

    def DibujarBoton(self, master):
        try:
            self.btn_guardar = Button(
                self.ventana, text="Insertar", relief="flat", background="#0051C8", cursor="hand1", foreground="white", command=lambda: self.insert(master)).place(x=750, y=340, width=90)
            self.btn_cancelar = Button(
                self.ventana, text="Cerrar", relief="flat", background="red", cursor="hand1", foreground="white", command=lambda: self.cancelar()).place(x=850, y=340, width=90)
            self.btn_buscar = Button(
                self.ventana, text="Filtrado Código", relief="flat", background="Green", cursor="hand1", foreground="white", command=lambda: self.buscarProvincia(self.buscar.get(), master)).place(x=260, y=339, width=100)

        except:
            messagebox.showinfo(title="Error",
                                message="Error al dibujar botón", parent=master)

    """
    Intenta vaciar la tabla y dibujar una nueva, pero si falla, muestra un mensaje de error
    
    @param ref es el nombre de la provincia
    @param master la ventana raíz
    """

    def buscarProvincia(self, ref, master):
        try:
            self.LimpiarTabla()
            self.DibujarTabla(ref)
        except print(0):
            messagebox.showinfo(title="Error",
                                message="Error al buscar la provincia", parent=master)

    """
    Crea una tabla y la llena con datos de una base de datos.
    
    @param ref La referencia a la ventana.
    """

    def DibujarTabla(self, ref):
        try:
            self.lista = ttk.Treeview(self.ventana, columns=(
                1, 2), show="headings", height="8")
            # estilos de tabla
            estilo = ttk.Style()
            estilo.theme_use("clam")
            estilo.configure("Treeview.Heading", background="#0051C8",
                             relief="flat", foreground="black")

            self.lista.heading(1, text="Codigo Postal")
            self.lista.heading(2, text="Nombre")
            self.lista.column(1, anchor=CENTER)
            self.lista.column(2, anchor=CENTER)
            self.lista.place(x=340, y=90, width=600)

            # Crear evento al hacer doble click en la tabla
            self.lista.bind("<Double 1>", self.obtenerFila)
            if ref == "":
                # Rellenar tabla
                d = ControlMySQL()
                elements = d.obtenerProvincias()
                for i in elements:
                    self.lista.insert('', 'end', values=i)
            else:
                # Rellenar tabla
                d = ControlMySQL()
                elements = d.buscarFiltroCodigo(ref)
                for i in elements:
                    self.lista.insert('', 'end', values=i)
        except:
            messagebox.showinfo(
                title="Error", message="Error al filtrar", parent=self.getMaster())

    """
    Toma los valores de los campos de entrada, verifica si el primero es un número y, si lo es, inserta
    los valores en la base de datos.
    
    @param master La ventana principal
    """

    def insert(self, master):
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
                    title="Error", message="Necesitas insertar un codigo", parent=master)
        except:
            messagebox.showinfo(title="Error",
                                message="Error al insertar", parent=master)

    """
    Elimina todas las filas en la vista de árbol.
    """

    def LimpiarTabla(self):
        try:
            self.lista.delete(*self.lista.get_children())
        except:
            pass

    """
    Es una función que abre una nueva ventana cuando haces clic en una fila de una tabla.
    
    @param event El evento que activó la devolución de llamada.
    """

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

            self.lbl_name = Label(pop, foreground="white",
                                  background="#24363e", text="Nombre", font=(8)).place(x=70, y=70)

            txt_n = Entry(pop, textvariable=nom, font=(8)
                          ).place(x=160, y=70, width=180)
            # botones
            btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                                command=lambda: self.editar(pop, c, nom.get())).place(x=70, y=140, width=90)

            btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                                  command=lambda: self.eliminarProvincia(pop, cod.get())).place(x=250, y=140, width=90)
        except:
            messagebox.showinfo(title="Base de Datos",
                                message="No se ha podido seleccionar la fila", parent=self.getMaster())

    """
    Toma el nombre de la provincia y el id de la provincia y actualiza la base de datos con el nuevo
    nombre.
    
    @param pop es la ventana que está abierta
    @param c es el id de la fila
    @param nombre El nombre de la provincia
    """

    def editar(self, pop, c, nombre):
        try:
            if nombre != "":
                j = ControlMySQL()
                j.UpdateItem(nombre, c)
                messagebox.showinfo(title="Crud Paqueteria",
                                    message="Editado", parent=pop)
                self.LimpiarTabla()
                self.DibujarTabla("")
                self.exitProgram(pop)

            else:
                messagebox.showinfo(title="Error",
                                    message="No dejes la provincia vacia", parent=pop)
        except:
            messagebox.showinfo(title="Error",
                                message="Error al editar", parent=pop)

    """
    Elimina una fila de una tabla en una base de datos.
    
    @param pop es la ventana que se abre
    @param n El número de la provincia a borrar
    """

    def eliminarProvincia(self, pop, n):
        try:
            int(n)
            if n != "":
                j = ControlMySQL()
                j.eliminarProvincia(n)
                messagebox.showinfo(title="Eliminar",
                                    message="Se ha actualizado la base  de datos", parent=pop)
                self.LimpiarTabla()
                self.DibujarTabla("")
                self.exitProgram(pop)

            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar un codigo", parent=pop)
        except:
            messagebox.showinfo(title="Error",
                                message="Error al eliminar", parent=pop)

    """
    La función cancelar() se llama cuando el usuario hace clic en el botón cancelar. Cierra la base de
    datos y muestra un mensaje.
    """

    def cancelar(self):
        try:
            self.getMaster().destroy()
            messagebox.showinfo(title="Base de Datos",
                                message="Se ha cerrado la base de datos de provincias")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al cerrar la base de datos de provincias")

    """
    Devuelve la ventana maestra.
    
    @return El objeto ventana.
    """

    def getMaster(self):
        return self.ventana

    """
    Crea una nueva ventana, establece su título, tamaño, posición y color de fondo, y luego crea una
    instancia de la clase App
    
    @return La ventana raíz.
    """


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
    root.config(background="#202931")
    App(root)
    return root
