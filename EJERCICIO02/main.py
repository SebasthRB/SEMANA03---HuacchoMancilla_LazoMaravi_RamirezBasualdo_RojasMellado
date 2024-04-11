from calificacion import CalificacionLiteral

if __name__=='__main__':
    print("\n\n\t\t CALIFICACIONES NUMÉRICAS Y LITERALES")
    print("\t\t------------------------------------------")
    
    calificacion=CalificacionLiteral()
    
    nota = float(input("\n\t Ingrese la nota del estudiante (0-10): Nota: -> "))
    
    calificacion.Calificacion(nota)