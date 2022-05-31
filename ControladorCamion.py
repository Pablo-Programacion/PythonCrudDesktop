import pymysql
import conexion as conexion
from ModeloCamion import *

# Es una clase que se conecta a una base de datos y realiza operaciones CRUD en ella.


class ControlMySQLCamion:
    d = Data3()

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertCamion(self, element):
        self.d.insertCamion(element)

    def obtenerCamion(self):
        return self.d.obtenerCamion()

    def buscarFiltroCodigo(self, ref):
        return self.d.buscarFiltroCodigo(ref)

    def eliminarCamion(self, ref):
        self.d.eliminarCamion(ref)

    def UpdateItem(self, potencia, modelo, tipo, ref):
        self.d.UpdateItem(potencia, modelo, tipo, ref)
