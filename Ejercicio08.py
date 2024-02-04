from metodos import info,advertencia,error,respuesta,fecha
"""
Ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato:
aaaammdd verificar si la fecha es correcta en sentido de numero de meses y días.

"""

def obtener_dia_mes_anio(fecha):
    # Obtener año, mes y día utilizando slicing de cadenas
    anio = int(fecha[0:4])
    mes = int(fecha[4:6])
    dia = int(fecha[6:8])

    return dia, mes, anio

def validar_fecha(fecha):
     # Extraer año, mes y día de la cadena
    year = int(fecha[0:4])
    month = int(fecha[4:6])
    day = int(fecha[6:8])

    # Verificar si el año, mes y día están en rangos válidos
    if (year < 1000 or year > 9999) or (month < 1 or month > 12) or (day < 1 or day > 31):
        return False

    # Verificar días en el mes
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar si el año es bisiesto
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        dias_por_mes[2] = 29

    if day > dias_por_mes[month]:
        return False

    return True

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar la fecha
        fecha_usuario = input(info("Ingrese un valor numerico de ocho digitos: "))

        # Verificar si la entrada tiene 8 dígitos
        if len(fecha_usuario) == 8 and fecha_usuario.isdigit():
            dia, mes, anio = obtener_dia_mes_anio(fecha_usuario)
            print(fecha(f"Día: {dia}"))
            print(fecha(f"Mes: {mes}"))
            print(fecha(f"Año: {anio}"))
        else:
            print(error("El formato de fecha es incorrecto. Ingrese una fecha válida de 8 dígitos."))
    except ValueError:
        print(advertencia("Por favor, ingrese una fecha numérica válida."))