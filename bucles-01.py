"""1.- Escribe una función que reciba una lista de 6 números enteros ingresados por
teclado e imprima cuales son pares, impares y a su vez si son primos o no.
al final retorna la suma de todos los números."""
numeros=[]
index=0
suma=0
for i in range(6):
    index+=1
    print("Ingresa el numero ",index,": ")
    valor=int(input())
    numeros.append(valor)

for i in range(6):
    if numeros[i] % 2==0:
        print(numeros[i],"Es par")
    if numeros[i] % 2!=0:
        print(numeros[i],"Es inpar")
    if numeros[i]==2 or numeros[i]==3:
        print(numeros[i]," Es primo")
    else:
        if numeros[i] % 2==0 or numeros[i] % 3==0:            
            print(numeros[i]," No es primo")
        else:
            print(numeros[i]," Es primo")
    print()
    suma+=numeros[i]

print("Suma total: ",suma)
