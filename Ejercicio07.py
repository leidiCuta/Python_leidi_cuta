from metodos import info,advertencia,error,respuesta
"""
Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot

"""
def calcular_ipotenusa():
    print("base del  primer cateto")
    print("base del segundo cateto")
def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar los catetos
        cateto1 = float(input(info("Ingrese la longitud del cateto 1: ")))
        cateto2 = float(input(info("Ingrese la longitud del cateto 2: ")))

        # Calcular la hipotenusa utilizando el Teorema de Pitágoras
        hipotenusa = calcular_hipotenusa(cateto1, cateto2)

        # Imprimir el resultado
        print(respuesta(f"La hipotenusa del triángulo es: {hipotenusa}"))
    except ValueError:
        print(error("Por favor, ingrese valores numéricos válidos."))