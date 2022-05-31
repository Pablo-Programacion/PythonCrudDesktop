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
