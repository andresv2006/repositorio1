
while True:
    print("***** Cine Estrella *****")
    print("Bienvenido al sistema de Cine Estrella")
    print("1. Ver cuántas entradas quedan")
    print("2. Comprar una cantidad de entradas")
    print("3. Devolver entradas")
    print("4. Salir del sistema")
    opc=input("sselecciona una opcion (1-4): ")
    if opc=="1":
        while True:
            print("cantidad de entradas disponibles: ",cantidad_entradas)
            break
    elif opc=="2":
        cantidad_entradas_comprar=int(input("ingrese la cantidad de entradas a comprar: "))
        if cantidad_entradas_comprar>cantidad_entradas:
            print("Cantidad de entradas insuficientes para su requerimiento, porfavor ingrese una cantidad menor")
            break
        elif cantidad_entradas_comprar<1:
          print ("cantidad no valida")
        else:
            cantidad_entradas=cantidad_entradas-cantidad_entradas_comprar
            print("entradas compradas con exito, cantidad de entradas disponibles: ",cantidad_entradas)
            entradas_vendidas=entradas_vendidas+cantidad_entradas_comprar
    elif opc=="3":
        devolución_entradas=int(input("ingrese entradas a devolver: "))
        while True:
            if devolución_entradas>cantidad_entradas_comprar or devolución_entradas<1:
                int(input("cantidad no valida, debe ser una cantidad menor a la que compro y mayor a 0"))
            else:
                print ("entradas devueltas con exito, cantidad de entradas disponibles: ",cantidad_entradas)
                cantidad_entradas=cantidad_entradas+devolución_entradas
                entradas_devueltas=entradas_devueltas+devolución_entradas
                break
    elif opc=="4":
        print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
        print("total de entradas vendidas: ",entradas_vendidas)
        print("total de entradas vendidas: ",entradas_devueltas)
        exit()
    else:
        print ("opcion no valida")
        break