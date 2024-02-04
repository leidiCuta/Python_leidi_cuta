from metodos import info,advertencia,error,respuesta
"""
 Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de
ocurrencias de dicho carácter en una cadena de caracteres.

"""
def contar_ocurrencias(caracter, cadena):
    # Utilizar el método count para contar las ocurrencias del carácter en la cadena
    return cadena.count(caracter)

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar un carácter
        char_usuario = input(info("Ingrese un carácter: "))

        # Verificar si se ingresó un solo carácter
        if len(char_usuario) == 1:
            # Solicitar al usuario ingresar una cadena de caracteres
            cadena_usuario = input(info("Ingrese una cadena de caracteres: "))

            # Contar las ocurrencias del carácter en la cadena
            cantidad_ocurrencias = contar_ocurrencias(char_usuario, cadena_usuario)

            # Mostrar el resultado
            print(respuesta(f"El carácter '{char_usuario}' aparece {cantidad_ocurrencias} veces en la cadena."))
        else:
            print(advertencia("Por favor, ingrese un solo carácter."))
    except Exception as e:
        print(error(f"Error: {e}"))