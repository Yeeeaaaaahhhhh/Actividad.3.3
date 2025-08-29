from random import*
opcionC=input(f"""Bienvenido a la maquina de ventas, 
presione S si quiere comprar algo o N si no: """)


cocaC,aguaN,Sabritas,chiclesM,takisF,galletasP,kitK,Snigger,cajitaF,Sahur = 10,10,5,3,5,4,3,5,1,1
cocaC_p, aguaN_p, Sabritas_p, chiclesM_p, takisF_p, galletasP_p, kitK_p, Snigger_p, cajitaF_p, Sahur_p = 20,10,15,30,25,20,30,30,100,250
saldo = 0
des_sorpresa = 1
des_mayoreo = 0.8
descuento_acertijo = 1
acertijo = ''
cantidad = 1

while opcionC == 'S':

    saldoA = int(input("Ingrese el saldo que desee: "))
    if saldoA == 0:
        saldo = saldo
        print("Su saldo es de ",saldo)
    elif saldoA >0 :
        saldo = saldoA + saldo
        print("Su saldo es de",saldo)
    else:
        #Nos lo va pedir la miss
        print("Tienes algun tipo de discapacidad?")

    opcion = int(input(f"""
    Binvenido a la maquina de ventas,  
    a continuacion un listado de nuestros productos
        
        INVENTARIO                      PRECIO      CANTIDAD
        1.-Coca Cola,                   ${cocaC_p}      \t{cocaC}
        2.-Agua natural,                ${aguaN_p}      \t{aguaN}
        3.-Sabritas,                    ${Sabritas_p}       \t{Sabritas}
        4.-Chicles de menta,            ${chiclesM_p}       \t{chiclesM}
        5.-Takis Fuego                  ${takisF_p}     \t{takisF}
        6.-Galletas principe            ${galletasP_p}      \t{galletasP}
        7.-Kit kat                      ${kitK_p}       \t{kitK}
        8.-Snicker                      ${Snigger_p}        \t{Snigger}
        9.-Cajita feliz                 ${cajitaF_p}    \t{cajitaF}
        10.-Muñeco de TungTungSahur     ${Sahur_p}      \t{Sahur}
        
        EXTRA
        11.-Sorpresa :3
        12.-Administrador
        13.-Salir
        
        Opcion: """))

    if 1 <= opcion <= 10:
        cantidad = int(input(f"""
        Cantidad: """))

    if opcion == 1:
        precio1 = cocaC_p*cantidad
        if saldo >=precio1 and cocaC >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio1}")
                precio1 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio1}")
                precio1 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio1
            print(f"Total: ${precio1}")
            print("Aqui tiene su Coca Cola, disfrutela, su saldo restante es de", "$",saldo)
            cocaC = cocaC -1
            print("El inventario restante de Coca Cola es de",cocaC)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 2:
        precio2 = aguaN_p*cantidad
        if saldo >=precio2 and aguaN >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio2}")
                precio2 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio2}")
                precio2 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio2
            print(f"Total: ${precio2}")
            print("Aqui tiene su Agua natural, disftrutela, su saldo restante es de", "$",saldo)
            aguaN = aguaN -1
            print("El inventario restante de Agua natural es de",aguaN)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 3:
        precio3 = Sabritas_p*cantidad
        if saldo >=precio3 and Sabritas >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio3}")
                precio3 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio3}")
                precio3 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio3
            print(f"Total: ${precio3}")
            print("Aqui tiene sus papas Sabritas, su saldo restante es de", "$",saldo)
            Sabritas = Sabritas -1
            print("El inventario de Sabritas es de",Sabritas)
        else:
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 4:
        precio4 = chiclesM_p*cantidad
        if saldo >=precio4 and chiclesM >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio4}")
                precio4 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio4}")
                precio4 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio4
            print(f"Total: ${precio4}")
            print("Aqui tiene sus chicles, su saldo restante es de", "$",saldo)
            chiclesM = chiclesM -1
            print("El inventario de chicles es de",chiclesM)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 5 :
        precio5 = takisF_p*cantidad
        if saldo >=precio5 and takisF >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio5}")
                precio5 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio5}")
                precio5 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio5
            print(f"Total: ${precio5}")
            print("Aqui tiene sus Takis, su saldo restante es de", "$",saldo)
            takisF = takisF -1
            print("El inventario de Takis es de",takisF)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 6:
        precio6 = galletasP_p*cantidad
        if saldo >= precio6 and galletasP >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio6}")
                precio6 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio6}")
                precio6 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio6
            print(f"Total: ${precio6}")
            print("Aqui tiene sus galletas, su saldo restante es de ", "$",saldo)
            galletasP = galletasP -1
            print("El inventario de galletas es de ",galletasP)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 7:
        precio7 = kitK_p*cantidad
        if saldo >=precio7  and kitK >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio7}")
                precio7 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio7}")
                precio7 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio7
            print(f"Total: ${precio7}")
            print("Aqui tiene su KitKat, su saldo restante es de ", "$",saldo)
            kitK = kitK -1
            print("El inventario de KitKat es de ",kitK)
        else:
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 8:
        precio8 = Snigger_p*cantidad
        if saldo >=precio8 and Snigger >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio8}")
                precio8 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio8}")
                precio8 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio8
            print(f"Total: ${precio8}")
            print("Aqui tiene su Snicker, su saldo restante es de ", "$",saldo)
            Snigger = Snigger -1
            print("El inventario de Snicker es de ",Snigger)
        else:
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 9:
        precio9 = cajitaF_p*cantidad
        if saldo >=precio9 and cajitaF >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio9}")
                precio9 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio9}")
                precio9 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio9
            print(f"Total: ${precio9}")
            print("Aqui tiene su cajita feliz parapapapa, su saldo restante es de ", "$",saldo)
            cajitaF = cajitaF -1
            print("El inventario de cajita es de ",cajitaF)
        else :
            print("Su saldo es insuficiente o no hay inventario")
    elif opcion == 10:
        precio10 = Sahur_p*cantidad
        if saldo >=precio10 and Sahur >= cantidad:
            if cantidad >= 3:
                print(f"Subtotal: ${precio10}")
                precio10 *= des_mayoreo
                print(f"""Felicidades, obtienes 20% de descuento 
                por mas de 3 objetos o mas del mismo""")
            if acertijo == 1201214:
                print(f"Subtotal: ${precio10}")
                precio10 *= descuento_acertijo
                print(f"Descuento por acertijo del {descuento_acertijo*100}%")
            saldo = saldo - precio10
            print(f"Total: ${precio10}")
            print("Felicidades usted a adquirido al grandioso TungTungSahur, su saldo restante es de ", "$",saldo)
            Sahur = Sahur -1
            print(f"El inventario de TungTungSahur es de {Sahur}")
        else:
            print("Su saldo es insuficiente o no hay inventario")

#Esta es la sorpresa, lo que hizo pablo
    elif opcion == 11:

        print('''Bienvenido a la sorpresa! Necesitas el codigo numerico correcto para poder avanzar.
        Primero resuelve un acertijo, despues encuentra la palabra en la sopa de letras.
        Una vez teniendo la respuesta, usa la palabra para encontrar el codigo 
        Pista: A = 1,
        Excluye la Ñ
        
        Acertijo: El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía.
        
        O U T A Z Q D
        U F K T M S Q
        P N F A B U P
        S E E U M J A
        B E V D X K U
        O I I E R J Z
        C J N T I I L''')
        acertijo = int(input("Ingrese el codigo aqui: "))
        if acertijo == 1201214:
            descuento_acertijo = round(uniform(0.1, 0.9),1)
            print(f"""Felicidades! Resolviste el acertijo! 
            Te haz ganado un {descuento_acertijo*100}% de descuento en todas tus compras""")

            #continue
        else:
            print("El codigo es incorrecto :(")

    elif opcion == 12:
        opcion2 = 0
        clave = int(input("Ingrese clave de acceso: "))
        if clave == 280825:
            print(f"""
            Clave correcta.
                """)
            while opcion2 != 3:
                print("""
                    Que deseas hacer?
                    1.- Editar inventario
                    2.- Editar precios
                    3.- Salir del administrador""")

                opcion2 = int(input("Opcion: "))

                if opcion2 == 1:
                    editar = 0
                    while editar != 11:
                        print(f"""
                Editar inventario
                
                Que elemento deseas editar
                
                INVENTARIO                      PRECIO      CANTIDAD
                1.-Coca Cola,                   ${cocaC_p}      \t{cocaC}
                2.-Agua natural,                ${aguaN_p}      \t{aguaN}
                3.-Sabritas,                    ${Sabritas_p}       \t{Sabritas}
                4.-Chicles de menta,            ${chiclesM_p}       \t{chiclesM}
                5.-Takis Fuego                  ${takisF_p}     \t{takisF}
                6.-Galletas principe            ${galletasP_p}      \t{galletasP}
                7.-Kit kat                      ${kitK_p}       \t{kitK}
                8.-Snicker                      ${Snigger_p}        \t{Snigger}
                9.-Cajita feliz                 ${cajitaF_p}    \t{cajitaF}
                10.-Muñeco de TungTungSahur     ${Sahur_p}      \t{Sahur}
                
                ingresa '11' para salir
                        """)

                        editar = int(input("Elemento: "))

                        if editar == 1:
                            print(f"el inventario actual de Coca cola es de {cocaC}")
                            cocaC_x = int(input("Cuantos elementos deseas agregar: "))
                            cocaC += cocaC_x
                            print(f"el inventario actual de Coca cola es de {cocaC}")

                        elif editar == 2:
                            print(f"el inventario actual de Agua natural es de {aguaN}")
                            aguaN_x = int(input("Cuantos elementos deseas agregar: "))
                            aguaN += aguaN_x
                            print(f"el inventario actual de Agua natural es de {aguaN}")

                        elif editar == 3:
                            print(f"el inventario actual de Sabritas es de {Sabritas}")
                            Sabritas_x = int(input("Cuantos elementos deseas agregar: "))
                            Sabritas += Sabritas_x
                            print(f"el inventario actual de Sabritas es de {Sabritas}")

                        elif editar == 4:
                            print(f"el inventario actual de Chicles de menta es de {chiclesM}")
                            chiclesM_x = int(input("Cuantos elementos deseas agregar: "))
                            chiclesM += chiclesM_x
                            print(f"el inventario actual de Chicles de menta es de {chiclesM}")

                        elif editar == 5:
                            print(f"el inventario actual de Takis Fuego es de {takisF}")
                            takisF_x = int(input("Cuantos elementos deseas agregar: "))
                            takisF += takisF_x
                            print(f"el inventario actual de Takis Fuego es de {takisF}")

                        elif editar == 6:
                            print(f"el inventario actual de Galletas principe es de {galletasP}")
                            galletasP_x = int(input("Cuantos elementos deseas agregar: "))
                            galletasP += galletasP_x
                            print(f"el inventario actual de Galletas principe es de {galletasP}")

                        elif editar == 7:
                            print(f"el inventario actual de Kit kat es de {kitK}")
                            kitK_x = int(input("Cuantos elementos deseas agregar: "))
                            kitK += kitK_x
                            print(f"el inventario actual de Kit kat es de {kitK}")

                        elif editar == 8:
                            print(f"el inventario actual de Snicker es de {Snigger}")
                            Snigger_x = int(input("Cuantos elementos deseas agregar: "))
                            Snigger += Snigger_x
                            print(f"el inventario actual de Snicker es de {Snigger}")

                        elif editar == 9:
                            print(f"el inventario actual de Cajita feliz es de {cajitaF}")
                            cajitaF_x = int(input("Cuantos elementos deseas agregar: "))
                            cajitaF += cajitaF_x
                            print(f"el inventario actual de Cajita feliz es de {cajitaF}")

                        elif editar == 10:
                            print(f"el inventario actual de Muñeco de TungTungSahur es de {Sahur}")
                            Sahur_x = int(input("Cuantos elementos deseas agregar: "))
                            Sahur += Sahur_x
                            print(f"el inventario actual de Muñeco de TungTungSahur es de {Sahur}")

                        elif editar == 11:
                            print(f"Regresando al submenu")

                        else:
                            print("Ocion no disponible")

                elif opcion2 == 2:
                    editar2 = 0
                    while editar2 != 11:
                        print(f"""
                            Editar inventario

                INVENTARIO                      PRECIO      CANTIDAD
                1.-Coca Cola,                   ${cocaC_p}      \t{cocaC}
                2.-Agua natural,                ${aguaN_p}      \t{aguaN}
                3.-Sabritas,                    ${Sabritas_p}       \t{Sabritas}
                4.-Chicles de menta,            ${chiclesM_p}       \t{chiclesM}
                5.-Takis Fuego                  ${takisF_p}     \t{takisF}
                6.-Galletas principe            ${galletasP_p}      \t{galletasP}
                7.-Kit kat                      ${kitK_p}       \t{kitK}
                8.-Snicker                      ${Snigger_p}        \t{Snigger}
                9.-Cajita feliz                 ${cajitaF_p}    \t{cajitaF}
                10.-Muñeco de TungTungSahur     ${Sahur_p}      \t{Sahur}

                ingresa '11' para salir
                            """)

                        editar2 = int(input("Elemento: "))

                        if editar2 == 1:
                            print(f"el precio actual de Coca cola es de ${cocaC_p}")
                            cocaC_p = int(input("Nuevo precio: "))
                            print(f"el precio nuevo de Coca cola es de ${cocaC_p}")

                        elif editar2 == 2:
                            print(f"el precio actual de Agua natural es de ${aguaN_p}")
                            aguaN_p = int(input("Nuevo precio: "))
                            print(f"el precio nuevo de Agua natural es de ${aguaN_p}")

                        elif editar2 == 3:
                            print(f"el precio actual de Sabritas es de ${Sabritas_p}")
                            Sabritas_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Sabritas es de ${Sabritas_p}")

                        elif editar2 == 4:
                            print(f"el precio actual de Chicles de menta es de ${chiclesM_p}")
                            chiclesM_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual Chicles de menta es de {chiclesM_p}")

                        elif editar2 == 5:
                            print(f"el inventario actual de Takis Fuego es de {takisF_p}")
                            takisF_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Takis Fuego es de {takisF_p}")

                        elif editar2 == 6:
                            print(f"el inventario actual de Galletas principe es de {galletasP_p}")
                            galletasP_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Galletas principe es de {galletasP_p}")

                        elif editar2 == 7:
                            print(f"el inventario actual de Kit kat es de {kitK_p}")
                            kitK_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Kit kat es de {kitK_p}")

                        elif editar2 == 8:
                            print(f"el inventario actual de Snicker es de {Snigger_p}")
                            Snigger_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Snicker es de {Snigger_p}")

                        elif editar2 == 9:
                            print(f"el inventario actual de Cajita feliz es de {cajitaF_p}")
                            cajitaF_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Cajita feliz es de {cajitaF_p}")

                        elif editar2 == 10:
                            print(f"el inventario actual de Muñeco de TungTungSahur es de {Sahur_p}")
                            Sahur_p = int(input("Nuevo precio: "))
                            print(f"el inventario actual de Muñeco de TungTungSahur es de {Sahur_p}")

                        elif editar2 == 11:
                            print(f"Regresando al submenu")

                        else:
                            print("Opcion no disponible")

                elif opcion2 == 3:
                    print("Volviendo al menu principal")

                else:
                    print("Opcion no disponible")

    elif opcion == 13:
        print("\nSaliendo....")
        break

    else:
            print("Opcion no valida")



    opcionC = input(f"""
    Quiere seguir comprando en la maquina?, 
    recuerde poner una 'S' para si o una 'N' para no: """)

while opcionC != 'S' and opcionC != 'N':
    print("Opcion no valida")
    opcionC = input(f"""
        Quiere seguir comprando en la maquina?, 
        recuerde poner una 'S' para si o una 'N' para no: """)

print("Gracias por utilizar la maquina de ventas, tenga un bonito dia")

#hola

#hola



