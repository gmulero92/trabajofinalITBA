import actualizar_datos
import visualizacion

print("\n BIENVENIDO - por GUIDO MULERO (DNI: 36.806.509")

def menu():
    opcion_menu = input("\n1. Actualización de datos \
        \n\n2. Visualización de datos \
        \n\nIngrese la opción deseada y presione Enter:")

    if opcion_menu == "1":
        actualizar_datos.actualizar_datos()

    elif opcion_menu == "2":
        opcion_submenu = input("\n1. Resumen \
        \n\n2. Gráfico de ticker \
        \n\nIngrese la opción deseada y presione Enter:")

        if opcion_submenu == "1":
            visualizacion.mostrar_resumen()
        elif opcion_menu == "2":
            visualizacion.mostrar_grafico()
        else:
            print ("\n Seleccione una opción válida")
    else:
        print ("\n Seleccione una opción válida")
        menu()

decision = True

while decision:
    menu()
    p_decision = input("\nOprima Enter para volver al menu principal o la tecla S y luego Enter para salir.").lower()

    if p_decision == "s":
        decision = False