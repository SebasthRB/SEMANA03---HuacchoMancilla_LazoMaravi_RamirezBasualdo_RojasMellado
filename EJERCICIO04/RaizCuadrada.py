
class CalculoRaizCuadrada:
    
    def raiz_cuadrada(self, numero):
        if numero < 0:
            raise ValueError("No existe el calculo de raiz para un número negativo")
        if numero == 0:
            return 0

        approx = numero / 2.0
        
        while True:
            siguiente_aprox = (approx + numero / approx) / 2.0
            if abs(siguiente_aprox - approx) < 0.0001:  # Precisión deseada
                return siguiente_aprox
            approx = siguiente_aprox