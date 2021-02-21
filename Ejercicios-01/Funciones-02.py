"""2.- Realiza una función llamada area_circulo(radio) que devuelva el área de un
círculo a partir de un radio. Calcula el área de un círculo de 5 de radio."""
def area_circulo(radio):
    area= 3.1416*(pow(radio,2))
    return area

radio= 5
print("Area del circulo: ", area_circulo(radio))