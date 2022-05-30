import pymysql
import conexion as conexion
from ModeloPaquete import *


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
        self.d.UpdateItem(descripcion, destinatario, direccion, fecha, dni_camionero, cod_provincia, c)
