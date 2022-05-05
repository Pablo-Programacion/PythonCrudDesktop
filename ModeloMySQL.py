import pymysql
import conexion


class Data:

    def __init__(self):
        self.conn = conexion.conectar('root', '')

        self.cursor = self.conn.cursor()

    def insertProvincia(self, element):
        # our element contend the name, age and the carreer of the student
        # in position 0, 1, 2
        sql = "insert into provincia(Codigo,Nombre) values('{}', '{}')".format(
            element[0], element[1])
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios

    def ReturnOneItem(self, ref):
        # we have ref like name of the element
        sql = "select * from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def obtenerProvincias(self):
        sql = "select * from provincia"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def Delete(self, ref):
        sql = "delete from persona where Nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, element, ref):
        # element contains the values and ref is the name of the item that we want change
        sql = "update provincia set Codigo = '{}',Nombre = '{}' where Codigo = '{}'".format(
            element[0], element[1], ref)
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios


'''
d = Data()		
users = d.obtenerProvincias()
for i in users:
	print(i)
'''
