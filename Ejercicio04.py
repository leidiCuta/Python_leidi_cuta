from metodos import info,respuesta,error,advertencia

"""
En este problema tenemos un único dato de entrada: un valor numérico entero que deberá 
ingresar el usuario. La salida del algoritmo será informar si el numero ingresado por el usuario es 
múltiplo de 2 y 3. Sabemos que un número es múltiplo de otro cuando al dividir estos dos 
números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir un 
mensaje informando las causas por las cuales no se podrá efectuar la operación.

"""

def verificar_multiplo():
    try:
        # Solicitar al usuario ingresar un número
        numero = int(input(info("Ingrese un número entero: ")))

        # Verificar si el número es negativo o cero
        if numero <= 0:
            print(advertencia("El número ingresado debe ser positivo y mayor de cero."))
            return

        # Verificar si el número es múltiplo de 2 y 3
        if numero % 2 == 0 and numero % 3 == 0:
            print(respuesta(f"El número {numero} es múltiplo de 2 y 3."))
        else:
            print(error(f"El número {numero} no es múltiplo de 2 y 3."))
    
    except ValueError:
        print(advertencia("Por favor, ingrese un número entero válido."))

if __name__ == "__main__":
    print(info("Bienvenidos al desarrollo del taller de logica de programación con Python"))
    print(info("Nombre: Leidi Lorena Cuta Pérez"))
    print(info("Ficha:  2670142"))
    print((""))
    verificar_multiplo()