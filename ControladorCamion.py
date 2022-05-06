import pymysql
import conexion
from ModeloCamion import *


class ControlMySQL:
    d = Data()

    def __init__(self):
        self.conn = conexion.conectar('root', '')

        self.cursor = self.conn.cursor()

    def insertCamion(self, element):
        self.d.insertCamion(element)

    def ReturnOneItem(self, ref):
        # we have ref like name of the element
        sql = "select * from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def obtenerCamion(self):
        return self.d.obtenerCamion()

    def eliminarCamion(self, ref):
        self.d.eliminarCamion(ref)

    def UpdateItem(self, element, ref):
        self.d.UpdateItem(element,ref)


