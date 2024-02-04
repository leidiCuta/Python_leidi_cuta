from metodos import info,advertencia,error,respuesta
"""
Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena.

"""
def capitalizar_frase(frase):
    # Verificar si la frase tiene al menos 5 palabras
    palabras = frase.split()
    if len(palabras) < 5:
        print("La frase debe tener al menos 5 palabras.")
        return

    # Capitalizar cada palabra en la frase
    frase_capitalizada = ' '.join(word.capitalize() for word in palabras)

    return frase_capitalizada

if __name__ == "__main__":
    try: 
         # Solicitar al usuario ingresar una frase de al menos 5 palabras
        frase_usuario = input(info("Ingrese una frase de al menos 5 palabras: "))

        # Verificar si la frase tiene al menos 5 palabras
        palabras_en_frase = len(frase_usuario.split())
        if palabras_en_frase >= 5:
        # Capitalizar la frase
            frase_capitalizada = frase_usuario.capitalize()
            # Mostrar la frase capitalizada
            print(respuesta("Frase capitalizada:"))
            print(respuesta(frase_capitalizada))
        else:
            print(advertencia("La frase debe tener al menos 5 palabras."))
    except Exception as e:
         print(error(f"Error: {e}"))