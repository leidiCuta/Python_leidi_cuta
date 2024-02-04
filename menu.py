from metodos import info,advertencia,error,texto_es_numero
import Ejercicio01
import Ejercicio02
import Ejercicio03
import Ejercicio04
import Ejercicio05
import Ejercicio06
import Ejercicio07
import Ejercicio08
import Ejercicio09
import Ejercicio10
import Ejercicio11
import Ejercicio12
import Ejercicio13
import Ejercicio14
import Ejercicio15
import Ejercicio16
def menu():
    while True:
        print(info("Seleccione un ejercicio a ejecutar:"))
        print(info("1) Cociente de 2 números:"))
        print(info("2) Número par o impar"))
        print(info("3) Calcular area del circulo "))
        print(info("4) Multiplos de 2 y 3"))
        print(info("5) Fecha en formato: aaaammdd"))
        print(info("6) Número mayor, Número medio, Número menor  "))
        print(info("7) Hipotenusa de un triángulo"))
        print(info("8) Verificación de fecha "))
        print(info("9) Mes correspondiente en texto"))
        print(info("10) Tiempo que ha invertido una persona en hacer un examen"))
        print(info("11) Número en orden inverso"))
        print(info("12) Número  capicúa"))
        print(info("13) Cadena de caracteres"))
        print(info("14) Determinación si una cadena de caracteres es palíndroma"))
        print(info("15) Número de 0 a 99 y mostrarlo escrito"))
        print(info("16) Frase de mínimo cinco palabras capitalizada"))
        print(info("30) Salir:"))

        print(info("Digite un numero:\n"))
        opcion=texto_es_numero(input())

        # Comprueba si la opción seleccionada por el usuario es válida.
        if not opcion:
            print(error("Intentelo nuevamente"))
        if opcion == 1:
            Ejercicio01.calcular_cociente()
        elif opcion == 2:
            Ejercicio02.numero_par_inpar()
        elif opcion == 3:
            Ejercicio03.calcular_area_circulo()
        elif opcion == 4:
            Ejercicio04.verificar_multiplo()
        elif opcion == 5:
            Ejercicio05.obtener_dia_mes_anio()
        elif opcion == 6:
            Ejercicio06.encontrar_mayor_medio_menor()
        elif opcion == 7:
            Ejercicio07.calcular_hipotenusa()
        elif opcion == 8:
            Ejercicio08
        elif opcion == 9:
            Ejercicio09
        elif opcion == 10:
            Ejercicio10.calcular_tiempo()
        elif opcion == 11:
            Ejercicio11
        elif opcion == 12:
            Ejercicio12
        elif opcion == 13:
            Ejercicio13
        elif opcion == 14:
            Ejercicio14
        elif opcion == 15:
            Ejercicio15
        elif opcion == 16:
            Ejercicio16
        elif opcion == 30:
            print("Programa finalizado...")
            exit(0)
        else:
            print(advertencia("Opción inválida. Intente nuevamente."))

if __name__ == "__main__":
    print(info("Bienvenidos al desarrollo del taller de logica de programación con Python"))
    print(info("Nombre: Leidi Lorena Cuta Pérez"))
    print(info("Ficha:  2670142"))
    print((""))
    menu()