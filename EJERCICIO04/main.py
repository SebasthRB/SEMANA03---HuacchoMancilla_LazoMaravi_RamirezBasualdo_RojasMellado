from RaizCuadrada import CalculoRaizCuadrada

raizCuadrada=CalculoRaizCuadrada()

try:
    print("\n\t\t Calculo de una raíz cuadrada usando iteraciones ")
    print("\t\t -----------------------------------------------")
    numero = float(input("\n\t Ingresa un número para calcular su raíz cuadrada: "))
    resultado = raizCuadrada.raiz_cuadrada(numero)
    print("\t La raíz cuadrada de", numero, "es aproximadamente:", resultado, "\n\n")
except ValueError as e:
    print(e)
except Exception as e:
    print("Ha ocurrido un error:", e)