"""4.- Realiza una función llamada intermedio(a, b) que a partir de dos números,
devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio
entre -12 y 24:"""
def relacion(a,b):
    punto_inter=(a+b)/2
    if (punto_inter>-12 and punto_inter<24):
        return "El punto intermedio esta en el rango"
    else:
        return "El punto intermedio esta fuera de rango"

a=int(input("Ingresa el primer numero: "))
b=int(input("Ingresa el segundo numero: "))
print("\n",relacion(a,b))