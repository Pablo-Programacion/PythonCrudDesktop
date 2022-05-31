# Importando el módulo pymysql, el módulo de conexión y el módulo ModeloPaquete.
import pymysql
import conexion as conexion
from ModeloPaquete import *

# Es una clase que se conecta a una base de datos MySQL y realiza operaciones CRUD en una tabla
# llamada "paquete".


class ControlMySQLPaquete:
    d = Data4()

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertPaquete(self, element):
        self.d.insertPaquete(element)

    def obtenerPaquete(self):
        return self.d.obtenerPaquete()

    def buscarFiltroCodigo(self, ref):
        return self.d.buscarFiltroCodigo(ref)

    def eliminarPaquete(self, ref):
        self.d.eliminarPaquete(ref)

    def UpdateItem(self, descripcion, destinatario, direccion, fecha, dni_camionero, cod_provincia, c):
        self.d.UpdateItem(descripcion, destinatario, direccion,
                          fecha, dni_camionero, cod_provincia, c)
