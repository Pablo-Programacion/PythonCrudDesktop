# Importando el módulo pymysql, el módulo de conexión y el módulo ModeloProvinciasL.
import pymysql
import conexion as conexion
from ModeloProvinciasL import *

# Es una clase que se conecta a una base de datos y luego llama a métodos de otra clase para realizar
# operaciones en la base de datos.

class ControlMySQL:
    d = Data()

    def __init__(self):
        self.conn = conexion.conectar('root', '')

        self.cursor = self.conn.cursor()

    def insertProvincia(self, element):
        self.d.insertProvincia(element)

    def obtenerProvincias(self):
        return self.d.obtenerProvincias()

    def buscarFiltroCodigo(self, ref):
        return self.d.buscarFiltroCodigo(ref)

    def eliminarProvincia(self, ref):
        self.d.eliminarProvincia(ref)

    def UpdateItem(self, nombre, ref):
        self.d.UpdateItem(nombre,ref)



