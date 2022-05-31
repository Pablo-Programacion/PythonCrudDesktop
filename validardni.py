
"""
    Comprueba si el último carácter de la cadena es una letra y si los primeros 8 caracteres son
    números. Si es así, comprueba si el último carácter es la letra correcta para los primeros 8
    caracteres

    @param dni El número de DNI a validar.

    @return Un valor booleano.
    """


def nifvalidator(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    nif = dni
    respuesta = False
    if (len(nif) == 9):
        letraControl = nif[8].upper()
        dni = nif[:8]
        if (len(dni) == len([n for n in dni if n in numeros])):
            if tabla[int(dni) % 23] == letraControl:
                respuesta = True
    return respuesta
