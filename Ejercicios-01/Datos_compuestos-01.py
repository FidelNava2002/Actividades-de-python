#1.- Realiza una función separar(lista) que tome una lista de números enteros
#desordenados y devuelva dos listas ordenadas. La primera con los números pares y la
#segunda con los números impares.

numeros= [4,1,3,6,2,5]

def separar(numeros):
    numeros_par=[]
    numeros_inpar=[]

    for i in range(6):
        if numeros[i] % 2==0:
            numeros_par.append(numeros[i])
        elif numeros[i] % 2!=0:
            numeros_inpar.append(numeros[i])

    numeros_par.sort()
    numeros_inpar.sort()
    par= len(numeros_par)
    inpar= len(numeros_inpar)

    for i in range(par):
        print(numeros_par[i])
    print()
    for i in range(inpar):
        print(numeros_inpar[i])

separar(numeros)
