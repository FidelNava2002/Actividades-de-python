"""5.- Proponer una representación con tuplas para las cartas de la baraja francesa.
Escribir una función poker que recibe cinco cartas de la baraja francesa e informe
(devuelva el valor lógico correspondiente) si esas cartas forman o no un poker (es
decir que hay 4 cartas con el mismo número)."""
import sys

cartas=('A', 'A', 'A', 'A', 'K')
cont=0;

for i in range(5):
    if cont==4:
      print("Se formo el ¡POKER!")
      sys.exit()
    else:
     cont=0
    for a in range(5):
        if cartas[i]==cartas[a]:
            cont+=1

print("No se formo el poker")