import pymysql
import conexion as conexion


class Data:

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertProvincia(self, element):
        sql = "insert into provincia(Codigo,Nombre) values('{}', '{}')".format(
            element[0], element[1])

        self.cursor.execute(sql)
        self.conn.commit()

    def buscarFiltroCodigo(self, ref):
        sql = "select * from provincia where Codigo = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def buscarFiltroNombre(self, ref):
        sql = "select * from provincia where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def obtenerProvincias(self):
        sql = "select * from provincia"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def eliminarProvincia(self, ref):
        sql = "delete from provincia where Codigo = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, nombre, ref):
        sql = "update provincia set Nombre = '{}' where Codigo = '{}'".format(
            nombre, ref)
        self.cursor.execute(sql)
        self.conn.commit()
