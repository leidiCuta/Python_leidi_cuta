from metodos import Texto_color,info,advertencia,error,respuesta

"""
En este problema debemos de definir una constante con el valor de PI como 3,1416 y 
tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser entero o 
flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo 
en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un 
mensaje informando las causas por las cuales no se podrá efectuar la operación.

"""

PI = 3.1416

def calcular_area_circulo(radio):
    if radio > 0:
        area = PI * radio**2
        return area
    elif radio == 0:
        return (respuesta("El radio no puede ser cero. Ingrese un  valor mayor de cero."))
    else:
        return(respuesta ("El radio no puede ser negativo. Ingrese un valor positivo."))
    
    # Solicitar al usuario ingresar el radio

if __name__ == "__main__": 
    try:
        radio = float(input(info("Ingrese el radio del círculo: ")))
            
        if radio ==0 and radio >0:print(error("El radio no puede ser mernor o igual a cero"))
        else:
            resultado = calcular_area_circulo(radio)
            print(advertencia(f"El área del círculo es: {resultado}"))
    except ValueError:
            print(error("Por favor, ingrese un valor numérico válido."))
