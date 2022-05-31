# Importando el módulo pymysql.
import pymysql

"""
    Se conecta a la base de datos.

    @param user El nombre de usuario para iniciar sesión.
    @param password La contraseña para el usuario.

    @return Un objeto de conexión.
    """


def conectar(user, password):
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="paqueteria"
    )


def desconectar(conexion):
    """
    Cierra la conexión a la base de datos.

    @param conexion El objeto de conexión.
    """
    conexion.close()
