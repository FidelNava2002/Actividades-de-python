"""1.- Escribe un programa que pida dos números enteros y que calcule su división,
escribiendo si la división es exacta o no."""
n1= int(input("Ingresa el primer numero: "))
n2= int(input("Ingresa el segundo numero: "))
while n2==0:
    print("\nNo se puede dividir entre 0")
    n2= int(input("Ingresa el segundo numero: "))

divi= n1/n2

if (divi % 2==0):
    print("\nEs una division exacta")
else:
    print("\nEs division inexacta")