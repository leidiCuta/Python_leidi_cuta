from metodos import info,advertencia,error,respuesta
"""
Dado un número (leído por teclado), que representa los segundos que ha invertido una
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido.
Imprima el resultado por pantalla.

"""
def calcular_tiempo(segundos):
    # Calcular horas, minutos y segundos
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60

    return horas, minutos, segundos

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar el número de segundos
        segundos = int(input(info("Ingrese el número de segundos: ")))

        # Verificar si la entrada es un número positivo
        if segundos < 0:
            print(error("Por favor, ingrese un número de segundos positivo."))
        else:
            # Calcular horas, minutos y segundos
            horas, minutos, segundos_restantes = calcular_tiempo(segundos)

            # Imprimir el resultado
            print(respuesta(f"Tiempo invertido: {horas} horas, {minutos} minutos y {segundos_restantes} segundos."))
    except ValueError:
        print(error("Por favor, ingrese un número entero válido."))