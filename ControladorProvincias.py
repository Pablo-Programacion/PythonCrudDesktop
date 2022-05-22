import pymysql
import conexion as conexion
from ModeloProvinciasL import *


class ControlMySQL:
    d = Data()

    def __init__(self):
        self.conn = conexion.conectar('root', '')

        self.cursor = self.conn.cursor()

    def insertProvincia(self, element):
        self.d.insertProvincia(element)

    def obtenerProvincias(self):
        return self.d.obtenerProvincias()

    def buscarFiltroCodigo(self, ref):
        return self.d.buscarFiltroCodigo(ref)

    def eliminarProvincia(self, ref):
        self.d.eliminarProvincia(ref)

    def UpdateItem(self, nombre, ref):
        self.d.UpdateItem(nombre,ref)



