from interes import Intereses

if __name__=='__main__':
    print("\n\n\t\t INTERESES DE UNA CUENTA BANCARIA ")
    print("\t\t -------------------------------- ")
    
    interes=Intereses()
    
    saldo = float(input("\n\t Ingrese el saldo: S/. "))
    
    if saldo <= 0:
        print("\n\t El saldo ingresado es incorrecto \n\n")
    elif saldo > 0 and saldo < 10000:
        CuentaFinal=interes.calcular_interes3anual(saldo)
        print("\n\t El saldo final de la cuenta es: S/. ", CuentaFinal)
    elif saldo > 10000:
        CuentaFinal=interes.calcular_intereses4anula(saldo)
        print("\t El saldo final de la cuenta es: S/. ", CuentaFinal, "\n\n")