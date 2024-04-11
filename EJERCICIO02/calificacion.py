
class CalificacionLiteral:
    def Calificacion(self, nota):
        if nota<0 or nota>10:
            return print("Nota ingresada no válida")
        elif nota>9 and nota <= 10:
            return print("\t Calificación obtenida: -> A: Excelente")
        elif nota>8 and nota>=9:
            return print("\t Calificación obtendia: -> B: Muy bien")
        elif nota>=7.5 and nota<=8:
            return print("\t Calificación obtenida: -> C: Bien")
        elif nota<7.5:
            return print("\t Calificación obtenida: -> R: Reprobado")