opc=1
figuras= {}
lista_cua=[]
lista_tri=[]
lista_circulo=[]

figuras["cuadrado"]=None
figuras["triangulo"]=None
figuras["circulo"]=None

res_area=0;
tri_res_area=0
circulo_res_area=0
res_per=0
tri_res_per=0
circulo_res_per=0

validacion=0
opcion=''


def main():
    print("\n1.- Crear figura\n2.- Listar una clasificación de figuras\
        \n3.- Listar todas las figuras\n4.- Mostrar suma de todas las áreas\
        \n5.- Mostrar la suma de todos los perímetros\
        \n6.- Limpiar lista\n0.- Salir\n")

def crear_cuadro(lado):
    global res_area,res_per
    res_area= area_cuadrado(lado)
    res_per= perimetro_cuadrado(lado)
    lista_cua.append("Cuadrado")
    lista_cua.append(res_area)
    lista_cua.append(res_per)
    figuras["cuadrado"]= lista_cua
def area_cuadrado(lado):
    area= lado * lado
    return area
def perimetro_cuadrado(lado):
    peri= lado*4
    return peri

def crear_triangulo(base,altu):
    global tri_res_area,tri_res_per
    tri_res_area= area_triangulo(base,altu)
    tri_res_per= perimetro_triangulo(base)
    lista_tri.append("Triangulo")
    lista_tri.append(tri_res_area)
    lista_tri.append(tri_res_per)
    figuras["triangulo"]= lista_tri
def area_triangulo(base,altu):
    area= (base*altu)/2
    return area
def perimetro_triangulo(base):
    peri= base*3
    return peri

def crear_circulo(radio):
    global circulo_res_area,circulo_res_per
    circulo_res_area= area_circulo(radio)
    circulo_res_per= perimetro_circulo(radio)
    lista_circulo.append("Circulo")
    lista_circulo.append(circulo_res_area)
    lista_circulo.append(circulo_res_per)
    figuras["circulo"]= lista_circulo
def area_circulo(radio):
    area= 3.1416*pow(radio,2)
    return area
def perimetro_circulo(radio):
    peri= 2*3.1416*radio
    return peri

def listar_clasificacion(opc2):
    if opc2==1:
        if figuras["cuadrado"]==None:
            print("\nNo existe información en cuadrado")
        else:
            print(figuras["cuadrado"])
    if opc2==2:
        if figuras["triangulo"]==None:
            print("\nNo existe información en triangulo")
        else:
            print(figuras["triangulo"])    
    if opc2==3:
        if figuras["circulo"]==None:
            print("\nNo existe información en circulo")
        else:
            print(figuras["circulo"])

def imprimir():
    if figuras["cuadrado"]!=None:
        print("Cuadrado: ",figuras["cuadrado"])
    if figuras["triangulo"]!=None:
        print("Triangulo: ",figuras["triangulo"])
    if figuras["circulo"]!=None:
        print("Circulo: ",figuras["circulo"])
    else:
        print("\nNo exite ningun dato")

def sumador_areas():
    suma_area=res_area + tri_res_area + circulo_res_area
    print("Suma total de area: ",suma_area)

def sumador_perimetros():
    suma_perimetro= res_per + tri_res_per + circulo_res_per
    print("Suma total de perimetros: ",suma_perimetro)

def limpiar():
    figuras["cuadrado"]=None
    figuras["triangulo"]=None
    figuras["circulo"]=None
    print("\nToda la informacion fue eliminada")


while opc!=0:
    main()
    opc=int(input("Elige una opcion: "))
    if opc==1:
        print("\n1.-Cuadrado\n2.-Triangulo\n3.-Circulo\n")
        opc1=int(input("Selecciona la figura: "))
        if opc1==1:
            lado=int(input("Ingresa el lado del cuadrado: \n"))
            crear_cuadro(lado)
        elif opc1==2:
            base=int(input("Ingresa la base del triangulo: "))
            altu= int(input("Ingresa la altura del triangulo: "))
            crear_triangulo(base,altu)
        elif opc1==3:
            radio= int(input("Ingresa el radio del circulo: "))
            crear_circulo(radio)
    if opc==2:
        while validacion!=1:
            print("\n1.-Cuadrado\n2.-Triangulo\n3.-Circulo\n")
            opcion=input("Selecciona la figura: ")
            if opcion=='1' or opcion=='2' or opcion=='3':
                opc2=int(opcion)
                validacion=1
            else:
                validacion=0
                print("\nOpcion no disponible")
        validacion=0
        listar_clasificacion(opc2)
    if opc==3:
        imprimir();
    if opc==4:
        sumador_areas()
    if opc==5:
        sumador_perimetros()
    if opc==6:
        limpiar()