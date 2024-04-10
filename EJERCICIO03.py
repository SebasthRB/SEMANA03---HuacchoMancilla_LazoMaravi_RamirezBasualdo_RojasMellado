import math

def sexagesimales_a_radianes(grados):
    respuesta_radianes = grados * math.pi / 180
    return respuesta_radianes

def radianes_a_sexagesimales(radianes):
    respuesta_sexagesimales = radianes * 180 / math.pi
    return respuesta_sexagesimales

# Conversión de grados a radianes
continuar = True

while continuar:
    grado_ingresado = float(input("Ingrese el valor del grado a transformar: "))
    opcion = ""

    while opcion not in ["1", "2"]:
        opcion = input(
            "Ingrese una de las siguientes opciones: (1) Sexagesimal a radianes || (2) Radianes a sexagesimal: ")

        if opcion == "1":
            grado_en_radianes = sexagesimales_a_radianes(grado_ingresado)
            print(f"{grado_ingresado} grados sexagesimales = {grado_en_radianes} radianes")
        elif opcion == "2":
            grado_en_sexagesimal = radianes_a_sexagesimales(grado_ingresado)
            print(f"{grado_ingresado} radianes = {grado_en_sexagesimal} grados sexagesimales")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    respuesta = ""
    while respuesta.lower() not in ["s", "n"]:
        respuesta = input("¿Desea continuar? (s/n): ")
        if respuesta.lower() == "n":
            continuar = False
        elif respuesta.lower() != "s":
            print("Opción no válida. Inténtalo de nuevo.")