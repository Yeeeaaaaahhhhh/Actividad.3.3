opcionC=input("""Bienvenido a la maquina de ventas, presione S si quiere comprar algo o N si no""")
cocaC,aguaN,Sabritas,chiclesM,takisF,galletasP,kitK,Snigger,cajitaF,Sahur = 10,10,5,3,5,4,3,5,1,1
saldo = 0
while opcionC == 'S':

    saldoA = int(input("Ingrese el saldo que desee"))
    if saldoA == 0:
        saldo = saldo
        print("Su saldo es de",saldo)
    elif saldoA >0 :
        saldo = saldoA + saldo
        print("Su saldo es de",saldo)
    else:
        #Nos lo va pedir la miss
        print("Tienes algun tipo de discapacidad?")
    opcion = int(input("""Binvenido a la maquina de ventas,  a continuacion un listado de nuestros productos
        1.-Coca Cola, $20, 10
        2.-Agua natural, $10, 10
        3.-Sabritas, $15, 5
        4.-Chicles de menta, $30, 3
        5.-Takis Fuego, $25, 5
        6.-Galletas principe, $20, 4
        7.-Kit kat, $30, 3
        8.-Snicker, $30, 5
        9.-Cajita feliz, $100, 1
        10.-Muñeco de TungTungSahur, $250, 1"""))
    if opcion == 1:
        if saldo >=20 and cocaC >0:
            saldo = saldo - 20
            print("Aqui tiene su Coca Cola, disfrutela, su saldo restante es de", "$",saldo)
            cocaC = cocaC -1
            print("El inventario restante de Coca Cola es de",cocaC)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 2:
        if saldo >=10 and aguaN >0:
            saldo = saldo - 10
            print("Aqui tiene su Agua natural, disftrutela, su saldo restante es de", "$",saldo)
            aguaN = aguaN -1
            print("El inventario restante de Agua natural es de",aguaN)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 3:
        if saldo >=15 and Sabritas >0:
            saldo = saldo - 15
            print("Aqui tiene sus papas Sabritas, su saldo restante es de", "$",saldo)
            Sabritas = Sabritas -1
            print("El inventario de Sabritas es de",Sabritas)
        else:
            print("Su saldo es insuficiente")
    elif opcion == 4:
        if saldo >=30 and chiclesM >0:
            saldo = saldo - 30
            print("Aqui tiene sus chicles, su saldo restante es de", "$",saldo)
            chiclesM = chiclesM -1
            print("El inventario de chicles es de",chiclesM)
        else :
            print("Su saldo es insuficiente")
    elif opcion == 5 :
        if saldo >=25 and takisF>0:
            saldo = saldo - 25
            print("Aqui tiene sus Takis, su saldo restante es de", "$",saldo)
            takisF = takisF -1
            print("El inventario de Takis es de",takisF)
        else :
            print("Su saldo es insuficiente")
    elif opcion == 6:
        if saldo >=20 and galletasP >0:
            saldo = saldo - 20
            print("Aqui tiene sus galletas, su saldo restante es de", "$",saldo)
            galletasP = galletasP -1
            print("El inventario de galletas es de",galletasP)
        else :
            print("Su saldo es insuficiente")
    elif opcion == 7:
        if saldo >=30  and kitK>0:
            saldo = saldo - 30
            print("Aqui tiene su KitKat, su saldo restante es de", "$",saldo)
            kitK = kitK -1
            print("El inventario de KitKat es de",kitK)
    elif opcion == 8:
        if saldo >=30 and Snigger>0:
            saldo = saldo - 30
            print("Aqui tiene su Snicker, su saldo restante es de", "$",saldo)
            Snigger = Snigger -1
            print("El inventario de Snicker es de",Snigger)
    elif opcion == 9:
        if saldo >=100 and cajitaF>0:
            saldo = saldo - 100
            print("Aqui tiene su cajita feliz parapapapa, su saldo restante es de", "$",saldo)
            cajitaF = cajitaF -1
            print("El inventario de cajita es de",cajitaF)
        else :
            print("Su saldo es insuficiente")
    elif opcion == 10:
        if saldo >=250 and Sahur>0:
            saldo = saldo - 250
            print("Felicidades usted a adquirido al grandioso TungTungSahur, su saldo restante es de", "$",saldo)
            Sahur = Sahur -1
        else :
            print("Su saldo es insuficiente")
    opcionC = input("Quiere seguir comprando en la maquina?, recuerde poner una S si si o una N si no")
print("Gracias por utilizar la maquina de ventas, tenga un bonito dia")





