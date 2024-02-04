from metodos import info,advertencia,error,respuesta,fecha
"""
 En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el
siguiente formato: aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2
dígitos representan el mes y los 2 dígitos restantes representan el día. Se pide informar por
separado el día, el mes y el año de la fecha ingresada. Para su solución se debe de hacer uso de
divisiones, operador modulo y conversión de double a entero

"""

def obtener_dia_mes_anio(fecha):
    # Convertir la fecha a entero
    fecha_entero = int(fecha)

    # Obtener año, mes y día utilizando divisiones y operador módulo
    anio = fecha_entero // 10000
    mes = (fecha_entero // 100) % 100
    dia = fecha_entero % 100

    return dia, mes, anio

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar la fecha
        fecha_usuario = input(info("Ingrese un valor numerico de ocho digitos: "))

        # Verificar si la entrada tiene 8 dígitos
        if len(fecha_usuario) == 8 and fecha_usuario.isdigit():
            dia, mes, ano = obtener_dia_mes_anio(fecha_usuario)
            print(fecha(f"Día: {dia}"))
            print(fecha(f"Mes: {mes}"))
            print(fecha(f"Año: {ano}"))
        else:
            print(respuesta("Formato de fecha incorrecto. Ingrese una fecha válida de 8 dígitos."))
    except ValueError:
        print(error("Por favor, ingrese una fecha numérica válida."))