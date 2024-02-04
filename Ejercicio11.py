from metodos import info,error,respuesta,fecha
"""
Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.

"""
def mostrar_digitos_inversos(numero):
    # Convertir el número a una cadena para facilitar el procesamiento de dígitos
    cadena_numero = str(numero)

    # Mostrar cada dígito en orden inverso
    for digito in reversed(cadena_numero):
        print(digito)

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar un número entero
        numero = int(input(info("Ingrese un número entero: ")))

        # Mostrar los dígitos en orden inverso
        print(respuesta("Dígitos en orden inverso:"))
        mostrar_digitos_inversos(fecha(numero))
    except ValueError:
        print(error("Por favor, ingrese un número entero válido."))