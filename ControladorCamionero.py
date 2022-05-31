# Importando el módulo pymysql, el módulo de conexión y el módulo ModeloCamionero.
import pymysql
import conexion as conexion
from ModeloCamionero import *

# Una clase que se conecta a una base de datos y realiza operaciones CRUD.


class ControlMySQLCamionero:
    d = Data2()

    def __init__(self):
        self.conn = conexion.conectar('root', '')
        self.cursor = self.conn.cursor()

    def insertCamionero(self, element):
        self.d.insertCamionero(element)

    def obtenerCamioneros(self):
        return self.d.obtenerCamioneros()

    def buscarFiltroCodigo(self, ref):
        return self.d.buscarFiltroCodigo(ref)

    def eliminarCamionero(self, ref):
        self.d.eliminarCamionero(ref)

    def UpdateItem(self, nombre, Telefono, Poblacion, Direccion, Salario, ref):
        self.d.UpdateItem(nombre, Telefono, Poblacion, Direccion, Salario, ref)
