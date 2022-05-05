import pymysql
import conexion


class Data:

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertCamion(self, element):
        # our element contend the name, age and the carreer of the student
        # in position 0, 1, 2
        sql = "insert into camion(Matricula,Potencia,Modelo,Tipo) values('{}', '{}', '{}', '{}')".format(
            element[0], element[1], element[2], element[3])
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios

    def buscarFiltroCodigo(self, ref):
        # we have ref like name of the element
        sql = "select * from provincia where Codigo = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def buscarFiltroNombre(self, ref):
        # we have ref like name of the element
        sql = "select * from provincia where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def obtenerCamion(self):
        sql = "select * from camion"
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
