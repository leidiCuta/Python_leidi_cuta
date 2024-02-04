from metodos import error,info,advertencia,texto_es_numero

"""
En este problema tenemos un único dato de entrada: un valor numérico entero que deberá 
ingresar el usuario. La salida del algoritmo será informar si el usuario ingresó un valor par o impar. 
Sabemos que un número par es aquel que es divisible por 2 o, también, que un número es par si el 
valor residual que se obtiene al dividirlo por 2 es cero. Según lo anterior, podremos informar que 
el número ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero. De 
lo contrario, informaremos que el número es impar.

"""
        

def numero_par_inpar():
    print(info("\n*** Informe del número ingresado ***"))

    try:
        numero = int(input(info("Ingrese un número: ")))
        
        
        if numero % 2 == 0:
            print(advertencia(f"El número {numero} es par."))
        else:
            print(advertencia(f"El número {numero} es impar."))
    
    except ValueError:
        print(error("Por favor, ingrese un número entero válido."))

if __name__ == "__main__":
    print(info("Bienvenidos al desarrollo del taller de logica de programación con Python"))
    print(info("Nombre: Leidi Lorena Cuta Pérez"))
    print(info("Ficha:  2670142"))
    print((""))
    numero_par_inpar()