from metodos import info,advertencia,error,respuesta,texto_es_numero
"""
Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe
de imprimir el mes correspondiente en texto

"""
def obtener_nombre_mes(numero_mes):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    return meses.get(numero_mes, "Mes no válido")

if __name__ == "__main__":
    
    try:
        
      while True:
        # Solicitar al usuario ingresar un número entre 1 y 12
        entrada_usuario = input(info("Ingrese un número entre 1 y 12: "))

        # Verificar si la entrada del usuario es un número
        if texto_es_numero(entrada_usuario):
            numero_mes = int(entrada_usuario)

            # Verificar si el número está en el rango válido
            if 1 <= numero_mes <= 12:
                nombre_mes = obtener_nombre_mes(numero_mes)
                print(respuesta(f"El mes correspondiente al número {numero_mes} es: {nombre_mes}"))
                break  # Salir del bucle si el número es válido
            else:
                print(error("Por favor, ingrese un número válido entre 1 y 12."))
        else:
            print(error("Por favor, ingrese un número."))
    except ValueError:
       print(advertencia("Por favor, ingrese un número entero válido."))
