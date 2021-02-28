"""3. - Escribe un programa que pida dos números y que conteste cuál es el menor y
cuál el mayor o que escriba que son iguales."""
n1=int(input("Ingresa el numero 1: "))
n2=int(input("Ingresa el numero 2: "))

if n1>n2:
    print(n1, "Es el mayor y ",n2,"es el menor")
elif n1<n2:
    print(n2, "Es el mayor y ",n1,"es el menor")
elif n1==n2:
    print("Los numeros son iguales")
    