# Importando el módulo pymysql y el módulo conexion.
import pymysql
import conexion as conexion

# Es una clase que se conecta a una base de datos y realiza operaciones CRUD en una tabla llamada
# camion.


class Data3:

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertCamion(self, element):
        sql = "insert into camion(Matricula,Potencia,Modelo,Tipo) values('{}', '{}', '{}', '{}')".format(
            element[0], element[1], element[2], element[3])
        self.cursor.execute(sql)
        self.conn.commit()

    def buscarFiltroCodigo(self, ref):
        sql = "select * from camion where matricula = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtenerCamion(self):
        sql = "select * from camion"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def eliminarCamion(self, ref):
        sql = "delete from camion where matricula = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self, potencia, modelo, tipo, ref):
        sql = "update camion set potencia = '{}',modelo = '{}',tipo = '{}' where matricula = '{}'".format(
            potencia, modelo, tipo, ref)
        self.cursor.execute(sql)
        self.conn.commit()
