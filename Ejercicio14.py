from metodos import info,advertencia,error,respuesta
"""
Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una
cadena se dice palíndromo si al invertirla es igual a ella misma.

"""
def es_palindromo(cadena):
    # Eliminar espacios y convertir la cadena a minúsculas para evitar diferencias de mayúsculas y minúsculas
    cadena = cadena.replace(" ", "").lower()

    # Verificar si la cadena es igual a su inverso
    return cadena == cadena[::-1]

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar una cadena de caracteres
        cadena_usuario = input(info("Ingrese una cadena de caracteres: "))

        # Verificar si la cadena es palíndroma
        if es_palindromo(cadena_usuario):
            print(respuesta("La cadena es palíndroma."))
        else:
            print(respuesta("La cadena no es palíndroma."))
    except Exception as e:
        print(error(f"Error: {e}"))