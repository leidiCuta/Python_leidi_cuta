
def Texto_color(texto: str, color:str):
    """
    Metodo para darle color a un texto

    :arg
    texto (str): texto al que se le a dar color.
    color (str): Color que se le va adar color .

    :return
    texto (str): El texto con el color dado 
    """
    ascii_color = "\033[39m {}\033[00m"
    if color == "negro":
        ascii_color = "\033[30m {}\033[00m"
    elif color == "rojo_oscuro":
        ascii_color = "\033[31m {}\033[00m"
    elif color == "verde_oscuro":
        ascii_color = "\033[32m {}\033[00m"
    elif color == "amarillo_oscuro":
        ascii_color = "\033[33m {}\033[00m"
    elif color == "azul_oscuro":
        ascii_color = "\033[34m {}\033[00m"
    elif color == "magenta_oscuro":
        ascii_color = "\033[35m {}\033[00m"
    elif color == "cyan_oscuro":
        ascii_color = "\033[36m {}\033[00m"
    elif color == "gris":
        ascii_color = "\033[37m {}\033[00m"
    elif color == "gris_oscuro":
        ascii_color = "\033[90m {}\033[00m"
    elif color == "rojo":
        ascii_color = "\033[91m {}\033[00m"
    elif color == "verde":
        ascii_color = "\033[92m {}\033[00m"
    elif color == "amarillo":
        ascii_color = "\033[93m {}\033[00m"
    elif color == "azul":
        ascii_color = "\033[94m {}\033[00m"
    elif color == "magenta":
        ascii_color = "\033[95m {}\033[00m"
    elif color == "cyan":
        ascii_color = "\033[96m {}\033[00m"
    elif color == "blanco":
        ascii_color = "\033[97m {}\033[00m"
    return ascii_color.format(texto)

def fecha(texto: str):
    return Texto_color(texto, color= "magenta")

def respuesta(texto: str):
    return Texto_color(texto, color= "azul")

def advertencia(texto: str):
    return Texto_color(texto, color="amarillo")

def info(texto: str):
    return Texto_color(texto, color="verde")

def error(texto: str):
    return Texto_color(texto, color="rojo")

def texto_es_numero(valor: str):
        while True:
            if valor.isnumeric():
                return int (valor)
            else:
                print(error(f"El texto {valor} no se puede convertir a numero "))
                print(advertencia("Ingrese nuevamente un numero "))
                valor = input()
            
   
       
def validar_numero_par(numero_1):
    if numero_1  % 2 == 0:
        print(advertencia(f"El número {numero_1} es par."))
        return int(numero_1)
    else:
        print(error(f"El número {numero_1} no es par. Inténtalo de nuevo."))
        print(advertencia("Ingrese un número par"))
        numero_1=validar_numero_par(int(input()))
        return
    
