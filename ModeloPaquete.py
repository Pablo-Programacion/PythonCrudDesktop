import pymysql
import conexion as conexion


class Data4:

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertPaquete(self, element):
        sql = "insert into paquete(codigo,descripcion,destinatario,direccion,fecha,dni_camionero,cod_provincia) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            element[0], element[1], element[2], element[3], element[4], element[5], element[6])
        self.cursor.execute(sql)
        self.conn.commit()

    def buscarFiltroCodigo(self, ref):
        sql = "select * from paquete where codigo = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtenerPaquete(self):
        sql = "select * from paquete"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def eliminarPaquete(self, ref):
        sql = "delete from paquete where codigo = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateItem(self,descripcion, destinatario, direccion, fecha, dni_camionero, cod_provincia, c):
        sql = "update paquete set descripcion = '{}',destinatario = '{}',direccion = '{}',fecha = '{}',dni_camionero = '{}',cod_provincia = '{}' where codigo = '{}'".format(
            descripcion, destinatario, direccion, fecha, dni_camionero, cod_provincia, c)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
