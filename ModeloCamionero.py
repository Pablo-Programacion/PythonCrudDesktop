# Importando el módulo pymysql y el módulo conexion.
import pymysql
import conexion as conexion

# Es una clase que se conecta a una base de datos y realiza operaciones CRUD en una tabla llamada
# camionero.


class Data2:

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertCamionero(self, element):
        sql = "insert into camionero(Dni,Nombre,Telefono,Poblacion,Direccion,Salario) values('{}', '{}', '{}', '{}', '{}', '{}')".format(
            element[0], element[1], element[2], element[3], element[4], element[5])

        self.cursor.execute(sql)
        self.conn.commit()

    def buscarFiltroCodigo(self, ref):
        sql = "select * from camionero where DNI = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtenerCamioneros(self):
        sql = "select * from camionero"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def eliminarCamionero(self, ref):
        sql = "delete from camionero where dni = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, nombre, Telefono, Poblacion, Direccion, Salario, ref):
        sql = "update camionero set Nombre = '{}',Telefono = '{}',Poblacion = '{}',Direccion = '{}',Salario = '{}' where Dni = '{}'".format(
            nombre, Telefono, Poblacion, Direccion, Salario, ref)
        self.cursor.execute(sql)
        self.conn.commit()
