import pymysql


def conectar(user, password):
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="paqueteria"
    )

def desconectar(conexion):
    conexion.close()