from metodos import info,advertencia,error,respuesta
"""
Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el
menor. Considerar que los tres valores serán diferentes

"""
def  encontrar_mayor_medio_menor(valor1, valor2, valor3):# utilise la tupla para valor1,valor2,valor3
    # Encontrar el mayor
    mayor = max(valor1, valor2, valor3)

    # Encontrar el menor
    menor = min(valor1, valor2, valor3)

    # Encontrar el del medio
    medio = (valor1 + valor2 + valor3) - mayor - menor

    return mayor, medio, menor

if __name__ == "__main__":
    try:
        # Solicitar al usuario ingresar tres valores enteros diferentes
        valor1 = int(input(info("Ingrese el primer valor entero: ")))
        valor2 = int(input(info("Ingrese el segundo valor entero: ")))
        valor3 = int(input(info("Ingrese el tercer valor entero: ")))

        # Verificar que los tres valores son diferentes
        if valor1 != valor2 != valor3:
            mayor, medio, menor = encontrar_mayor_medio_menor(valor1, valor2, valor3)
            print(respuesta(f"El mayor es: {mayor}"))
            print(respuesta(f"El del medio es: {medio}"))
            print(respuesta(f"El menor es: {menor}"))
        else:
            print(error("Por favor, ingrese tres valores diferentes."))
    except ValueError:
        print(advertencia("Por favor, ingrese valores enteros válidos."))
