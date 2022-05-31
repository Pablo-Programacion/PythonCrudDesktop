# Importación de los módulos necesarios para la ejecución del programa.
from doctest import master
from tkinter import messagebox
import tkinter
from click import style
from tkinter import *
from tkinter import ttk
from ControladorCamion import *

"""
    Crea una ventana con un título y un color de fondo.

    @return La ventana raíz.
    """


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
    Crea una etiqueta para cada uno de los cuatro atributos de la clase.
    
    @param master La ventana principal.
    """

    def DibujarLabel(self, master):
        try:
            self.lbl_nombre_general = Label(self.ventana, foreground="white",
                                            background="#202931", text="CAMION", font=(20)).place(x=1000, y=30)
            self.lbl_matricula = Label(self.ventana, foreground="white",
                                       background="#202931", text="Matricula", font=(8)).place(x=20, y=70)
            self.lbl_potencia = Label(self.ventana, foreground="white",
                                      background="#202931", text="Potencia", font=(8)).place(x=20, y=110)
            self.lbl_modelo = Label(self.ventana, foreground="white",
                                    background="#202931", text="Modelo", font=(8)).place(x=20, y=150)
            self.lbl_tipo = Label(self.ventana, foreground="white",
                                  background="#202931", text="Tipo", font=(8)).place(x=20, y=190)
        except:
            messagebox.showinfo(title="Error",
                                message="No se pudieron dibujar los labels", parent=master)

    """
    Crea un montón de objetos StringVar, luego crea un montón de widgets de entrada y luego los coloca
    en la pantalla.
    
    @param master La ventana principal.
    """

    def DibujarEntry(self, master):
        try:
            self.matricula = StringVar()
            self.potencia = StringVar()
            self.modelo = StringVar()
            self.tipo = StringVar()
            self.buscar = StringVar()

            self.txt_matricula = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.matricula).place(x=120, y=70)
            self.txt_potencia = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.potencia).place(x=120, y=110)
            self.txt_modelo = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.modelo).place(x=120, y=150)
            self.txt_tipo = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.tipo).place(x=120, y=190)
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
                self.ventana, text="Insertar", relief="flat", background="#0051C8", cursor="hand1", foreground="white", command=lambda: self.insert(master)).place(x=1550, y=340, width=90)
            self.btn_cancelar = Button(
                self.ventana, text="Cerrar", relief="flat", background="red", cursor="hand1", foreground="white", command=lambda: self.cancelar()).place(x=1650, y=340, width=90)
            self.btn_buscar = Button(
                self.ventana, text="Filtrado Código", relief="flat", background="Green", cursor="hand1", foreground="white", command=lambda: self.buscarCamionero(self.buscar.get(), master)).place(x=260, y=339, width=100)

        except:
            messagebox.showinfo(title="Error",
                                message="Error al dibujar botón", parent=master)

    """
    Se busca a un camionero.
    
    @param ref es la referencia del camionero
    @param master la ventana raíz
    """

    def buscarCamionero(self, ref, master):
        try:
            self.LimpiarTabla()
            self.DibujarTabla(ref)
        except print(0):
            messagebox.showinfo(title="Error",
                                message="Error al buscar el camion", parent=master)

    """
    Crea una tabla con los datos de la base de datos.
    
    @param ref La referencia al widget, en este caso, la vista de árbol.
    """

    def DibujarTabla(self, ref):
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
            self.lista.place(x=340, y=90, width=1400)

            # Crear evento al hacer doble click en la tabla
            self.lista.bind("<Double 1>", self.obtenerFila)
            if ref == "":
                # Rellenar tabla
                d = ControlMySQLCamion()
                elements = d.obtenerCamion()
                for i in elements:
                    self.lista.insert('', 'end', values=i)
            else:
                # Rellenar tabla
                d = ControlMySQLCamion()
                elements = d.buscarFiltroCodigo(ref)
                for i in elements:
                    self.lista.insert('', 'end', values=i)
        except Exception as e:
            messagebox.showinfo(
                title="Error al dibujar la tabla", message=e, parent=self.getMaster())

    """
    Toma los valores de los widgets de entrada y los inserta en la base de datos.
    
    @param master La ventana principal
    """

    def insert(self, master):
        try:
            int(self.potencia.get())
            if self.matricula.get() != "":
                arr = [self.matricula.get(), self.potencia.get(), self.modelo.get(
                ), self.tipo.get()]
                c = ControlMySQLCamion()
                c.insertCamion(arr)
                self.matricula.set("")
                self.potencia.set("")
                self.modelo.set("")
                self.tipo.set("")
                self.LimpiarTabla()
                self.DibujarTabla("")
            else:
                messagebox.showinfo(
                    title="Error", message="Necesitas insertar la matricula", parent=master)
        except Exception as e:
            messagebox.showinfo(title="Error",
                                message="Indica la potencia mediante un numero", parent=master)

    """
    Elimina todas las filas en la vista de árbol.
    """

    def LimpiarTabla(self):
        try:
            self.lista.delete(*self.lista.get_children())
        except:
            pass

    """
    Una función que le permite editar los datos de una fila en una tabla.
    
    @param event El evento que activó la devolución de llamada.
    """

    def obtenerFila(self, event):
        try:
            matricula = StringVar()
            potencia = StringVar()
            modelo = StringVar()
            tipo = StringVar()
            nombreFila = self.lista.identify_row(event.y)
            elemento = self.lista.item(self.lista.focus())
            d = elemento['values'][0]
            n = elemento['values'][1]
            t = elemento['values'][2]
            p = elemento['values'][3]

            matricula.set(d)
            potencia.set(n)
            modelo.set(t)
            tipo.set(p)

            pop = Toplevel(self.ventana)
            pop.title("Editar camionero")
            # Centrar ventana en el medio
            ancho_ventana = 400
            alto_ventana = 300
            x_ventana = pop.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = pop.winfo_screenheight() // 2 - alto_ventana // 2
            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
                "+" + str(x_ventana) + "+" + str(y_ventana)
            pop.geometry(posicion)
            pop.resizable(0, 0)
            pop.config(background="#24363e")
            self.lbl_potencia = Label(pop, foreground="white",
                                      background="#24363e", text="Potencia", font=(8)).place(x=70, y=70)
            self.lbl_modelo = Label(pop, foreground="white",
                                    background="#24363e", text="Modelo", font=(8)).place(x=70, y=100)
            self.lbl_tipo = Label(pop, foreground="white",
                                  background="#24363e", text="Tipo", font=(8)).place(x=70, y=130)

            txt_n = Entry(pop, textvariable=potencia, font=(8)
                          ).place(x=160, y=70, width=180)
            txt_t = Entry(pop, textvariable=modelo, font=(8)
                          ).place(x=160, y=100, width=180)
            txt_p = Entry(pop, textvariable=tipo, font=(8)
                          ).place(x=160, y=130, width=180)
            # botones
            btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                                command=lambda: self.editar(pop, d, potencia.get(), modelo.get(), tipo.get())).place(x=70, y=240, width=90)

            btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                                  command=lambda: self.eliminarCamionero(pop, matricula.get())).place(x=250, y=240, width=90)
        except:
            messagebox.showinfo(title="Base de Datos",
                                message="No se ha podido seleccionar la fila", parent=self.getMaster())

    """
    Toma los valores de los cuadros de entrada y actualiza la base de datos con ellos.
    
    @param pop La ventana que se está editando.
    @param c la clave principal de la tabla
    @param potencia En t
    @param modelo VarCadena()
    @param tipo tipo de camión
    """

    def editar(self, pop, c, potencia, modelo, tipo):
        try:
            int(potencia)
            if modelo != "" or tipo != "":
                j = ControlMySQLCamion()
                j.UpdateItem(potencia, modelo, tipo, c)
                messagebox.showinfo(title="Crud Paqueteria",
                                    message="Editado", parent=pop)
                self.LimpiarTabla()
                self.DibujarTabla("")
                self.exitProgram(pop)
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar el modelo y el tipo", parent=pop)

        except Exception as e:
            messagebox.showinfo(title="Error",
                                message="Los valores introducidos son invalidos", parent=pop)

    """
    Elimina una fila de una tabla en una base de datos.
    
    @param pop es la ventana que se abre
    @param n la identificación del conductor
    """

    def eliminarCamionero(self, pop, n):
        try:
            if n != "":

                j = ControlMySQLCamion()
                j.eliminarCamion(n)
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
    Devuelve el objeto de ventana que se creó cuando se instancia la clase
    """

    def cancelar(self):
        try:
            self.getMaster().destroy()
            messagebox.showinfo(title="Base de Datos",
                                message="Se ha cerrado la base de datos de provincias")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al cerrar la base de datos de provincias")

    def getMaster(self):
        return self.ventana

    """
    Crea una ventana con un título y un color de fondo.
    
    @return La ventana raíz.
    """


def configCamion():
    root = tkinter.Toplevel()
    root.title("Crud Paqueteria")
    # Centrar ventana en el medio
    ancho_ventana = 1800
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
