from doctest import master
from tkinter import messagebox
import tkinter
from click import style
from tkinter import *
from tkinter import ttk
from ControladorPaquete import *

"""
    @return Se está devolviendo la ventana raíz.
    """


class App:

    root = 0

    """
    Crea una ventana con una etiqueta, una entrada, un botón y una tabla.
    
    @param master La ventana principal.
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
    Crea un montón de etiquetas.
    
    @param master La ventana principal.
    """

    def DibujarLabel(self, master):
        try:
            self.lbl_nombre_general = Label(self.ventana, foreground="white",
                                            background="#202931", text="PAQUETE", font=(20)).place(x=1000, y=30)
            self.lbl_codigo = Label(self.ventana, foreground="white",
                                    background="#202931", text="Codigo", font=(8)).place(x=20, y=40)
            self.lbl_descripcion = Label(self.ventana, foreground="white",
                                         background="#202931", text="Descripcion", font=(8)).place(x=20, y=80)
            self.lbl_Destinatario = Label(self.ventana, foreground="white",
                                          background="#202931", text="Destinatario", font=(8)).place(x=20, y=120)
            self.lbl_direccion = Label(self.ventana, foreground="white",
                                       background="#202931", text="Direccion", font=(8)).place(x=20, y=160)
            self.lbl_Fecha = Label(self.ventana, foreground="white",
                                   background="#202931", text="Fecha", font=(8)).place(x=20, y=200)
            self.lbl_Dni_camionero = Label(self.ventana, foreground="white",
                                           background="#202931", text="Dni camionero", font=(8)).place(x=20, y=240)
            self.lbl_cod_provincia = Label(self.ventana, foreground="white",
                                           background="#202931", text="Cod provincia", font=(8)).place(x=20, y=280)
        except:
            messagebox.showinfo(title="Error",
                                message="No se pudieron dibujar los labels", parent=master)

    """
    Crea un montón de widgets de entrada y los coloca en la pantalla.
    
    @param master La ventana principal.
    """

    def DibujarEntry(self, master):
        try:
            self.codigo = StringVar()
            self.descripcion = StringVar()
            self.destinatario = StringVar()
            self.direccion = StringVar()
            self.fecha = StringVar()
            self.dni_camionero = StringVar()
            self.cod_provincia = StringVar()
            self.buscar = StringVar()

            self.txt_codigo = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.codigo).place(x=130, y=40)
            self.txt_descripcion = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.descripcion).place(x=130, y=80)
            self.txt_destinatario = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.destinatario).place(x=130, y=120)
            self.txt_direccion = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.direccion).place(x=130, y=160)
            self.txt_fecha = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.fecha).place(x=130, y=200)
            self.txt_dni_camionero = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.dni_camionero).place(x=130, y=240)
            self.txt_cod_provincia = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.cod_provincia).place(x=130, y=280)

            # Agregación de buscar
            self.txt_buscar = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.buscar).place(x=60, y=340)

        except:
            messagebox.showinfo(title="Error",
                                message="Error en los entrys", parent=master)

    """
    Cierra la ventana
    
    @param window La ventana que desea cerrar.
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
    
    @param ref es el número de referencia del paquete
    @param master la ventana raíz
    """

    def buscarCamionero(self, ref, master):
        try:
            self.LimpiarTabla()
            self.DibujarTabla(ref)
        except print(0):
            messagebox.showinfo(title="Error",
                                message="Error al buscar el paquete", parent=master)

    """
    Crea una tabla con los datos de la base de datos.
    
    @param ref la referencia a la ventana principal
    """

    def DibujarTabla(self, ref):
        try:
            self.lista = ttk.Treeview(self.ventana, columns=(
                1, 2, 3, 4, 5, 6, 7), show="headings", height="8")
            # estilos de tabla
            estilo = ttk.Style()
            estilo.theme_use("clam")
            estilo.configure("Treeview.Heading", background="#0051C8",
                             relief="flat", foreground="black")

            self.lista.heading(1, text="Codigo")
            self.lista.heading(2, text="Descripcion")
            self.lista.heading(3, text="Destinatario")
            self.lista.heading(4, text="Direccion")
            self.lista.heading(5, text="Fecha")
            self.lista.heading(6, text="Dni Camionero")
            self.lista.heading(7, text="Cod Provincia")

            self.lista.column(1, anchor=CENTER)
            self.lista.column(2, anchor=CENTER)
            self.lista.column(3, anchor=CENTER)
            self.lista.column(4, anchor=CENTER)
            self.lista.column(5, anchor=CENTER)
            self.lista.column(6, anchor=CENTER)
            self.lista.column(7, anchor=CENTER)
            self.lista.place(x=340, y=90, width=1400)

            # Crear evento al hacer doble click en la tabla
            self.lista.bind("<Double 1>", self.obtenerFila)
            if ref == "":
                # Rellenar tabla
                d = ControlMySQLPaquete()
                elements = d.obtenerPaquete()
                for i in elements:
                    self.lista.insert('', 'end', values=i)
            else:
                # Rellenar tabla
                d = ControlMySQLPaquete()
                elements = d.buscarFiltroCodigo(ref)
                for i in elements:
                    self.lista.insert('', 'end', values=i)
        except Exception as e:
            messagebox.showinfo(
                title="Error al dibujar la tabla", message=e, parent=self.getMaster())

    """
    Toma una lista de valores y los inserta en una base de datos.
    
    @param master la ventana raíz
    """

    def insert(self, master):
        try:

            int(self.codigo.get())
            if self.codigo.get() != "":
                arr = [self.codigo.get(), self.descripcion.get(), self.destinatario.get(
                ), self.direccion.get(), self.fecha.get(), self.dni_camionero.get(), self.cod_provincia.get()]
                c = ControlMySQLPaquete()
                c.insertPaquete(arr)
                self.codigo.set("")
                self.descripcion.set("")
                self.destinatario.set("")
                self.direccion.set("")
                self.fecha.set("")
                self.dni_camionero.set("")
                self.cod_provincia.set("")
                self.LimpiarTabla()
                self.DibujarTabla("")
            else:
                messagebox.showinfo(
                    title="Error", message="Necesitas insertar un codigo", parent=master)
        except Exception as e:
            messagebox.showinfo(title="Error",
                                message="El codigo debe ser numerico", parent=master)

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
            codigo = StringVar()
            descripcion = StringVar()
            destinatario = StringVar()
            direccion = StringVar()
            fecha = StringVar()
            dni_camionero = StringVar()
            cod_provincia = StringVar()

            nombreFila = self.lista.identify_row(event.y)
            elemento = self.lista.item(self.lista.focus())
            d = elemento['values'][0]
            n = elemento['values'][1]
            t = elemento['values'][2]
            o = elemento['values'][3]
            p = elemento['values'][4]
            q = elemento['values'][5]
            t = elemento['values'][6]

            codigo.set(d)
            descripcion.set(n)
            destinatario.set(t)
            direccion.set(o)
            fecha.set(p)
            dni_camionero.set(q)
            cod_provincia.set(t)

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

            self.lbl_Descripcion = Label(pop, foreground="white",
                                         background="#24363e", text="Descripcion", font=(8)).place(x=70, y=60)
            self.lbl_Destinatario = Label(pop, foreground="white",
                                          background="#24363e", text="Destinatario", font=(8)).place(x=70, y=90)
            self.lbl_Direccion = Label(pop, foreground="white",
                                       background="#24363e", text="Direccion", font=(8)).place(x=70, y=120)
            self.lbl_Fecha = Label(pop, foreground="white",
                                   background="#24363e", text="Fecha", font=(8)).place(x=70, y=150)
            self.lbl_Dni_Camionero = Label(pop, foreground="white",
                                           background="#24363e", text="Dni Camionero", font=(8)).place(x=70, y=180)
            self.lbl_Cod_Provincia = Label(pop, foreground="white",
                                           background="#24363e", text="Cod Provincia", font=(8)).place(x=70, y=210)

            txt_t = Entry(pop, textvariable=descripcion, font=(8)
                          ).place(x=180, y=60, width=180)
            txt_p = Entry(pop, textvariable=destinatario, font=(8)
                          ).place(x=180, y=90, width=180)
            txt_o = Entry(pop, textvariable=direccion, font=(8)
                          ).place(x=180, y=120, width=180)
            txt_y = Entry(pop, textvariable=fecha, font=(8)
                          ).place(x=180, y=150, width=180)
            txt_u = Entry(pop, textvariable=dni_camionero, font=(8)
                          ).place(x=180, y=180, width=180)
            txt_i = Entry(pop, textvariable=cod_provincia, font=(8)
                          ).place(x=180, y=210, width=180)
            # botones

            ''' 
                        descripcion.set(n)
            destinatario.set(t)
            direccion.set(o)
            fecha.set(p)
            dni_camionero.set(q)
            cod_provincia.set(t)
            
             '''
            btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                                command=lambda: self.editar(pop, d, descripcion.get(), destinatario.get(), direccion.get(), fecha.get(), dni_camionero.get(), cod_provincia.get())).place(x=70, y=240, width=90)

            btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                                  command=lambda: self.eliminarPaquete(pop, codigo.get())).place(x=250, y=240, width=90)
        except:
            messagebox.showinfo(title="Base de Datos",
                                message="No se ha podido seleccionar la fila", parent=self.getMaster())

    """
    Toma los valores de los cuadros de entrada y actualiza la base de datos con ellos.
    
    @param pop La ventana que se abre
    @param c codigo
    @param descripcion Cuerda
    @param destinatario cuerda
    @param direccion Cuerda
    @param fecha fecha
    @param dni_camionero cuerda
    @param cod_provincia es una clave foránea
    """

    def editar(self, pop, c, descripcion, destinatario, direccion, fecha, dni_camionero, cod_provincia):
        try:
            int(c)
            if destinatario != "" or dni_camionero != "" or cod_provincia != "":
                j = ControlMySQLPaquete()
                j.UpdateItem(descripcion, destinatario, direccion,
                             fecha, dni_camionero, cod_provincia, c)
                messagebox.showinfo(title="Crud Paqueteria",
                                    message="Editado", parent=pop)
                self.LimpiarTabla()
                self.DibujarTabla("")
                self.exitProgram(pop)
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar el destinatario,dni camionero y cod provincia", parent=pop)

        except Exception as e:
            messagebox.showinfo(title="Error",
                                message="Los valores introducidos son invalidos", parent=pop)

    """
    Elimina una fila de una tabla en una base de datos.
    
    @param pop es la ventana que se abre
    @param n El nombre del paquete
    """

    def eliminarPaquete(self, pop, n):
        try:
            if n != "":

                j = ControlMySQLPaquete()
                j.eliminarPaquete(n)
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
    Cierra la base de datos.
    """

    def cancelar(self):
        try:
            self.getMaster().destroy()
            messagebox.showinfo(title="Base de Datos",
                                message="Se ha cerrado la base de datos de paquetes")
        except:
            messagebox.showinfo(title="Error",
                                message="Error al cerrar la base de datos de paquetes")

    """
    Devuelve la ventana maestra.
    
    @return El objeto ventana.
    """

    def getMaster(self):
        return self.ventana

    """
    Crea una ventana con un título, un tamaño y un color de fondo.
    
    @return La ventana raíz.
    """


def configPaquete():
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
