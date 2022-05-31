from doctest import master
from tkinter import messagebox
import tkinter
from click import style
from tkinter import *
from tkinter import ttk
from ControladorCamionero import *
from validardni import *

class App:
    root = 0

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

    def DibujarLabel(self, master):
        try:
            self.lbl_nombre_general = Label(self.ventana, foreground="white",
                                            background="#202931", text="CAMIONEROS", font=(20)).place(x=1000, y=30)
            self.lbl_dni = Label(self.ventana, foreground="white",
                                 background="#202931", text="DNI", font=(8)).place(x=20, y=70)
            self.lbl_nombre = Label(self.ventana, foreground="white",
                                    background="#202931", text="Nombre", font=(8)).place(x=20, y=110)
            self.lbl_telefono = Label(self.ventana, foreground="white",
                                      background="#202931", text="Teléfono", font=(8)).place(x=20, y=150)
            self.lbl_poblacion = Label(self.ventana, foreground="white",
                                       background="#202931", text="Población", font=(8)).place(x=20, y=190)
            self.lbl_direccion = Label(self.ventana, foreground="white",
                                       background="#202931", text="Dirección", font=(8)).place(x=20, y=230)
            self.lbl_salario = Label(self.ventana, foreground="white",
                                     background="#202931", text="Salario", font=(8)).place(x=20, y=270)
        except:
            messagebox.showinfo(title="Error",
                                message="No se pudieron dibujar los labels", parent=master)

    def DibujarEntry(self, master):
        try:
            self.dni = StringVar()
            self.nombre = StringVar()
            self.telefono = StringVar()
            self.poblacion = StringVar()
            self.direccion = StringVar()
            self.salario = StringVar()
            self.buscar = StringVar()

            self.txt_dni = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.dni).place(x=120, y=70)
            self.txt_nombre = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.nombre).place(x=120, y=110)
            self.txt_telefono = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.telefono).place(x=120, y=150)
            self.txt_poblacion = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.poblacion).place(x=120, y=190)
            self.txt_direccion = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.direccion).place(x=120, y=230)
            self.txt_salario = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.salario).place(x=120, y=270)
            # Agregación de buscar
            self.txt_buscar = Entry(self.ventana, font=(
                'Arial', 12), textvariable=self.buscar).place(x=60, y=340)

        except:
            messagebox.showinfo(title="Error",
                                message="Error en los entrys", parent=master)

    def exitProgram(self, window):
        window.destroy()
        window.update()

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

    def buscarCamionero(self, ref, master):
        try:
            self.LimpiarTabla()
            self.DibujarTabla(ref)
        except print(0):
            messagebox.showinfo(title="Error",
                                message="Error al los camioneros", parent=master)

    def DibujarTabla(self, ref):
        try:
            self.lista = ttk.Treeview(self.ventana, columns=(
                1, 2, 3, 4, 5, 6), show="headings", height="8")
            # estilos de tabla
            estilo = ttk.Style()
            estilo.theme_use("clam")
            estilo.configure("Treeview.Heading", background="#0051C8",
                             relief="flat", foreground="black")

            self.lista.heading(1, text="Dni")
            self.lista.heading(2, text="Nombre")
            self.lista.heading(3, text="Telefono")
            self.lista.heading(4, text="Población")
            self.lista.heading(5, text="Dirección")
            self.lista.heading(6, text="Salario")
            self.lista.column(1, anchor=CENTER)
            self.lista.column(2, anchor=CENTER)
            self.lista.column(3, anchor=CENTER)
            self.lista.column(4, anchor=CENTER)
            self.lista.column(5, anchor=CENTER)
            self.lista.column(6, anchor=CENTER)
            self.lista.place(x=340, y=90, width=1400)

            # Crear evento al hacer doble click en la tabla
            self.lista.bind("<Double 1>", self.obtenerFila)
            if ref == "":
                # Rellenar tabla
                d = ControlMySQLCamionero()
                elements = d.obtenerCamioneros()
                for i in elements:
                    self.lista.insert('', 'end', values=i)
            else:
                # Rellenar tabla
                d = ControlMySQLCamionero()
                elements = d.buscarFiltroCodigo(ref)
                for i in elements:
                    self.lista.insert('', 'end', values=i)
        except Exception as e:
            messagebox.showinfo(
                title="Error", message=e, parent=self.getMaster())

    def insert(self, master):
        try:
            int(self.telefono.get())
            int(self.salario.get())
            if self.dni.get() != "" and nifvalidator(self.dni.get()) == True :
                arr = [self.dni.get(), self.nombre.get(), self.telefono.get(
                ), self.poblacion.get(), self.direccion.get(), self.salario.get()]
                c = ControlMySQLCamionero()
                c.insertCamionero(arr)
                self.dni.set("")
                self.nombre.set("")
                self.telefono.set("")
                self.poblacion.set("")
                self.direccion.set("")
                self.salario.set("")
                self.LimpiarTabla()
                self.DibujarTabla("")
            else:
                messagebox.showinfo(
                    title="Error", message="Necesitas insertar un dni valido", parent=master)
        except Exception as e:
            messagebox.showinfo(title="Error",
                                message="Error el telefono y salario debe de ser numerico", parent=master)

    def LimpiarTabla(self):
        try:
            self.lista.delete(*self.lista.get_children())
        except:
            pass

    def obtenerFila(self, event):
        try:
            dni = StringVar()
            nombre = StringVar()
            telefono = StringVar()
            poblacion = StringVar()
            direccion = StringVar()
            salario = StringVar()

            nombreFila = self.lista.identify_row(event.y)
            elemento = self.lista.item(self.lista.focus())
            d = elemento['values'][0]
            n = elemento['values'][1]
            t = elemento['values'][2]
            p = elemento['values'][3]
            di = elemento['values'][4]
            s = elemento['values'][5]

            dni.set(d)
            nombre.set(n)
            telefono.set(t)
            poblacion.set(p)
            direccion.set(di)
            salario.set(s)

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

            self.lbl_name = Label(pop, foreground="white",
                                  background="#24363e", text="Nombre", font=(8)).place(x=70, y=70)
            self.lbl_telefono = Label(pop, foreground="white",
                                      background="#24363e", text="Telefono", font=(8)).place(x=70, y=100)
            self.lbl_poblacion = Label(pop, foreground="white",
                                       background="#24363e", text="Población", font=(8)).place(x=70, y=130)
            self.lbl_direccion = Label(pop, foreground="white",
                                       background="#24363e", text="Dirección", font=(8)).place(x=70, y=160)
            self.lbl_salario = Label(pop, foreground="white",
                                     background="#24363e", text="Salarios", font=(8)).place(x=70, y=190)

            txt_n = Entry(pop, textvariable=nombre, font=(8)
                          ).place(x=160, y=70, width=180)
            txt_t = Entry(pop, textvariable=telefono, font=(8)
                          ).place(x=160, y=100, width=180)
            txt_p = Entry(pop, textvariable=poblacion, font=(8)
                          ).place(x=160, y=130, width=180)
            txt_di = Entry(pop, textvariable=direccion, font=(8)
                           ).place(x=160, y=160, width=180)
            txt_s = Entry(pop, textvariable=salario, font=(8)
                          ).place(x=160, y=190, width=180)
            # botones
            btn_editar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white",
                                command=lambda: self.editar(pop, d, nombre.get(), telefono.get(), poblacion.get(), direccion.get(), salario.get())).place(x=70, y=240, width=90)

            btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white",
                                  command=lambda: self.eliminarCamionero(pop, dni.get())).place(x=250, y=240, width=90)
        except:
            messagebox.showinfo(title="Base de Datos",
                                message="No se ha podido seleccionar la fila", parent=self.getMaster())

    def editar(self, pop, c, nombre, telefono, poblacion, direccion, salario):
        try:
            if nombre != "":
                j = ControlMySQLCamionero()
                j.UpdateItem(nombre, telefono, poblacion,
                             direccion, salario, c)
                messagebox.showinfo(title="Crud Paqueteria",
                                    message="Editado", parent=pop)
                self.LimpiarTabla()
                self.DibujarTabla("")
                self.exitProgram(pop)
            else:
                messagebox.showinfo(title="Error",
                                    message="Necesitas insertar un nombre", parent=pop)

        except Exception as e:
            messagebox.showinfo(title="Error",
                                message=e, parent=pop)

    def eliminarCamionero(self, pop, n):
        try:
            if n != "":

                j = ControlMySQLCamionero()
                j.eliminarCamionero(n)
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


def configCamionero():
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
