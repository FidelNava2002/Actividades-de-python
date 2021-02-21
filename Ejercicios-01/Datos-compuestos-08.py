"""8.- Escribir una función dia_siguiente_t que dada una fecha expresada como la terna
(Día, Mes, Año) (donde Día y Año son números enteros, y Mes es el texto Ene, Feb, ...,
Dic, según corresponda) calcule el día siguiente al dado, en el mismo formato."""
dia=int(input("Ingresa numero de dia: "))
mes= input("Ingresa el mes(Ene,Feb,Mar...): ")
anio= int(input("Ingresa un año: "))
contar30=0
contar31=0
mses=0
def dia_siguiente_t(dia,mes,anio):
    mes31= ["Ene","Mar","May","Jul","Ago","Oct"]
    mes30= ["Abr","Jun","Sep","Nov"]
    meses= ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
    contar30=mes30.count(mes)
    contar31=mes31.count(mes)
    if (dia==30 and contar30==1):
        dia=1
        mses=(meses.index(mes))+1
        print(f"{dia} - {meses[mses]} - {anio}")
    elif(dia==31 and contar31==1):
        dia=1
        mses=(meses.index(mes))+1
        print(f"{dia} - {meses[mses]} - {anio}")
    elif(dia==28 and mes=="Feb"):
        dia=1
        mses=(meses.index(mes))+1
        print(f"{dia} - {meses[mses]} - {anio}")
    elif(dia==31 and mes=="Dic"):
        dia=1
        mes="Ene"
        anio+=1
        print(f"{dia} - {mes} - {anio}")
    else:
        dia+=1
        print(f"{dia} - {mes} - {anio}")


dia_siguiente_t(dia,mes,anio)