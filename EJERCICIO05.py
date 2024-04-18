import turtle

def dibuja_cuadrado(TAMAÑO_CUADRADO):
    colores = ["red", "green", "blue", "skyblue", "yellow"]
    
    for i in range(500):
        if TAMAÑO_CUADRADO <= 0:
            break
        
        turtle.color(colores[i%5])
        turtle.forward(TAMAÑO_CUADRADO)
        turtle.right(90)
        TAMAÑO_CUADRADO -= 2

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Dibujo de cuadrado usando turtle")


TAMAÑO_CUADRADO = int(input("Ingrese el decremento de tamaño: "))

dibuja_cuadrado(TAMAÑO_CUADRADO)

turtle.speed(10)  # Velocidad máxima de dibujo

# Mantener la ventana abierta
turtle.done()
