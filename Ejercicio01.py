from metodos import error,info,advertencia,texto_es_numero,validar_numero_par

"""
Ejercicio 1

En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a 
través del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora 
bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En 
este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así 
que tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar 
la operación

"""
def calcular_cociente():
    print("")
    print(info(" Calculadora de cociente : *"))

    print(info("Ingrese el primer numero"))
    numero_1 = validar_numero_par(int(input()))


    print(info("Ingrese el segundo numero"))
    numero_2 =texto_es_numero(input())
    


    if numero_2 == 0:
        print(error(" La divisición por 0 es una identación"))
    else:
        resultado = numero_1 / numero_2
        print(info(f"El resultado del cociente es:{resultado} *"))

if __name__ == "__main__":
    print(info("Bienvenidos al desarrollo del taller de logica de programación con Python"))
    print(info("Nombre: Leidi Lorena Cuta Pérez"))
    print(info("Ficha:  2670142"))
    print((""))
    calcular_cociente()
