"""4.- Escribe un programa que pida dos números enteros y que escriba si el mayor es
múltiplo del menor."""
n1=int(input("Ingresa el numero 1: "))
n2=int(input("Ingresa el numero 2: "))

if n1>n2:
    if n1%n2==0:
        print(n1," Es multiplo de ",n2)
elif n2>n1:
    if n2%n1==0:
        print(n2," Es multiplo de ",n1)