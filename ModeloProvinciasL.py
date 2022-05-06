import pymysql
import conexion


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
        # we have ref like name of the element
        sql = "select * from provincia where Codigo = '{}'".format(ref)
        print(sql)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchall()

    def buscarFiltroNombre(self, ref):
        # we have ref like name of the element
        sql = "select * from provincia where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def obtenerProvincias(self):
        sql = "select * from provincia"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def eliminarProvincia(self, ref):
        sql = "delete from provincia where Codigo = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, element, ref):
        # element contains the values and ref is the name of the item that we want change
        sql = "update provincia set Codigo = '{}',Nombre = '{}' where Codigo = '{}'".format(
            element[0], element[1], ref)
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios
