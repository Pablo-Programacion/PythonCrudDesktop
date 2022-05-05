import pymysql
import conexion
from ModeloMySQL import *


class ControlMySQL:
    d = Data()

    def __init__(self):
        self.conn = conexion.conectar('root', '')

        self.cursor = self.conn.cursor()

    def insertProvincia(self, element):
        self.d.insertProvincia(element)

    def ReturnOneItem(self, ref):
        # we have ref like name of the element
        sql = "select * from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def obtenerProvincias(self):
        self.d.obtenerProvincias()

    def Delete(self, ref):
        sql = "delete from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, element, ref):
         self.d.UpdateItem(element,ref)


'''
d = Data()		
users = d.obtenerProvincias()
for i in users:
	print(i)
'''
