from metodos import info,advertencia,error,respuesta,fecha
""""
Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el
número de cifras sea par y verificar si el número es capicúa o no.

"""
def es_capicua(numero):
    # Convertir el número a una cadena para facilitar la comparación
    cadena_numero = str(numero)

    # Verificar si la cadena es igual a su reverso
    return cadena_numero == cadena_numero[::-1]

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar un número
        numero = int(input(info("Ingrese un número: ")))

        # Verificar si el número de cifras es par
        if len(str(numero)) % 2 == 0:
            print(fecha("El número de cifras es par."))

            # Verificar si el número es capicúa
            if es_capicua(numero):
                print(respuesta("El número es capicúa."))
            else:
                print(respuesta("El número no es capicúa."))
        else:
            print(error("El número de cifras no es par."))
    except ValueError:
        print(advertencia("Por favor, ingrese un número entero válido."))