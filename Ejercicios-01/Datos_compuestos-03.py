"""3.- Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
mayor."""
loteria= []
suma=0
Valor=0
for i in range(5):
    suma+=1
    print("Ingresa el numero ",suma,": ")
    valor= int(input())
    loteria.append(valor)

loteria.sort()
print(loteria)
