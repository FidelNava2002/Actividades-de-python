"""7.- Escribir una función dia_siguiente_e que dada una fecha expresada como la terna
(Día, Mes, Año) (donde Día, Mes y Año son números enteros) calcule el día siguiente
al dado, en el mismo formato."""

dia=int(input("Ingresa numero de dia: "))
mes= int(input("Ingresa un mes en numero: "))
anio= int(input("Ingresa un año: "))
contar30=0
contar31=0
def dia_siguiente_e(dia,mes,anio):
    mes31= [1,3,5,7,8,10]
    mes30= [4,6,9,11]
    contar30=mes30.count(mes)
    contar31=mes31.count(mes)
    if (dia==30 and contar30==1):
        dia=1
        mes+=1
        print(f"{dia} - {mes} - {anio}")
    elif(dia==31 and contar31==1):
        dia=1
        mes+=1
        print(f"{dia} - {mes} - {anio}")
    elif(dia==28 and mes==2):
        dia=1
        mes+=1
        print(f"{dia} - {mes} - {anio}")
    elif(dia==31 and mes==12):
        dia=1
        mes=1
        anio+=1
        print(f"{dia} - {mes} - {anio}")
    else:
        dia+=1
        print(f"{dia} - {mes} - {anio}")


dia_siguiente_e(dia,mes,anio)