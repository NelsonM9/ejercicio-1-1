prestamo = int(input("ingrese cuanto es el monto del prestamo"))
plazo = int(input("ingrese a cuntos meses quiere dejar el prestamo"))
cuota = ((prestamo/plazo)*0.027)+(prestamo/plazo)
print("la cuota queda de el siguente valor: " + str(cuota))
