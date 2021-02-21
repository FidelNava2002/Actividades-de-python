"""6.- El tiempo como tuplas.
1. Proponer una representación con tuplas para representar el tiempo.
2. Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva
su suma."""

tiempo1= int((input("Ingresa minutos: ")))
tiempo2= int((input("Ingresa minutos: ")))

def sumaTiempo(tiempo1,tiempo2):
    suma= tiempo1 + tiempo2
    if suma<=59:
        print("El tiempo es: ",suma," minutos")
    else:
        hora= int(suma/60)
        resta= suma-(60*hora)
        print("El tiempo es: ",hora," horas ",resta," minutos")



sumaTiempo(tiempo1,tiempo2)

