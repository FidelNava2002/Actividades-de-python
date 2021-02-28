"""5.- Escribe un programa que pida tres números y que escriba si son los tres iguales,
si hay dos iguales o si son los tres distintos."""
n1=int(input("Ingresa el numero 1: "))
n2=int(input("Ingresa el numero 2: "))
n3=int(input("Ingresa el numero 3: "))

if n1==n2 and n1==n3:
    print("Los numeros son iguales")
elif n1==n2 or n1==n3:
    print("Hay dos numeros iguales")
elif n2==n1 or n2==n3:
    print("Hay dos numeros iguales")
else:
    print("Todos los numeros son distintos")