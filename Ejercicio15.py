from metodos import info,advertencia,error,respuesta

"""
Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y
seis.

"""
def num_a_palabra(num):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if num < 10:
        return unidades[num]
    elif num < 20:
        return especiales[num - 10]
    else:
        unidad = num % 10
        decena = num // 10
        return f"{decenas[decena]} {unidades[unidad]}".strip()

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar un número entre 0 y 99
        numero_usuario = int(input(info("Ingrese un número entre 0 y 99: ")))

        # Verificar si el número está en el rango adecuado
        if 0 <= numero_usuario <= 99:
            # Mostrar la representación escrita del número
            representacion_escrita = num_a_palabra(numero_usuario)
            print(respuesta(f"Representación escrita: {representacion_escrita}"))
        else:
            print(advertencia("Por favor, ingrese un número válido entre 0 y 99."))
    except ValueError:
        print(error("Por favor, ingrese un número entero válido."))