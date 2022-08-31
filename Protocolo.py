Titulo = []
listaP = []
listaSP = []
listaSSP = []
listaT = []

def AñadirPaso(opcAP):
    try:
        menuAP = int(input('''Seleccione como desea agregar
    1. Agregar
    2. Insertar
    3. Salir\n'''))
    except ValueError:
        menuAP = 0
    if (menuAP == 1 or menuAP == 2):
        try:
            listaP.append(0)
            listaSP.append(0)
            listaSSP.append(0)
            listaT.append(0)
            if (opcAP == 1):
                numPa = 1
                numPo = 0
                for i in range(0,len(listaP)):
                    if (numPa == listaP[i]):
                        numPa += 1
                if(menuAP == 1):
                    elementoNP = numPa
                else:
                    elementoNP = int(input("¿En que posicion quiere insertar el Paso? [1-" + str(numPa) + "]\n"))
                if (elementoNP >= 1 and elementoNP <= numPa):
                    if (elementoNP == 1):
                        numPo = 0
                    elif (elementoNP == numPa):
                        numPo = len(listaP)
                    else:
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo = i
                                break
                    elementoT = str(input("Ingrese el texto del paso\n"))
                    listaP.insert(numPo, elementoNP)
                    listaSP.insert(numPo, 0)
                    listaSSP.insert(numPo, 0)
                    listaT.insert(numPo, elementoT)
                    numRP = (numPo + 1)
                    for i in range (numRP,len(listaP)):
                        txtN = (listaP[i] + 1)
                        listaP.pop(i)
                        listaP.insert(i, txtN)
                else:
                    print("Intente de nuevo")
            elif (opcAP == 2):
                if (len(listaP) > 1):
                    numPa = 1
                    numPo1 = 0
                    numPo2 = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿En que Paso quiere agregar el SubPaso? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo1 = i
                                for i in range (numPo1,len(listaP)):
                                    if (elementoNP == listaP[i]):
                                        elementoNP = elementoNP
                                    else:
                                        numPo2 = i
                                        break
                                break
                        numPo1 += 1
                        numPo2 += 1
                        numSPa = 1
                        numSPo = 0
                        for i in range(numPo1,numPo2):
                            if (numSPa == listaSP[i]):
                                numSPa += 1
                        if(menuAP == 1):
                            elementoNSP = numSPa
                        else:
                            elementoNSP = int(input("¿En que posicion quiere agregar el SubPaso? [1-" + str(numSPa) + "]\n"))
                        if (elementoNSP >= 1 and elementoNSP <= numSPa):
                            if (elementoNSP == 1):
                                numSPo = numPo1
                            elif (elementoNSP == numSPa):
                                numSPo = numPo2 - 1
                            else:
                                for i in range (numPo1,numPo2):
                                    if (elementoNSP == listaSP[i]):
                                        numSPo = i
                                        break
                            elementoT = str(input("Ingrese el texto del Subpaso\n"))
                            listaP.insert(numSPo, elementoNP)
                            listaSP.insert(numSPo, elementoNSP)
                            listaSSP.insert(numSPo, 0)
                            listaT.insert(numSPo, elementoT)
                            numRP = (numSPo + 1)
                            for i in range (numRP,numPo2):
                                txtN = (listaSP[i] + 1)
                                listaSP.pop(i)
                                listaSP.insert(i, txtN)
                        else:
                            print("Intente de nuevo")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos donde poner Subpasos")
            elif (opcAP == 3):
                if (len(listaP) > 1):
                    numPa = 1
                    numPo1 = 0
                    numPo2 = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿En que Paso quiere agregar el SubSubPaso? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo1 = i
                                for i in range (numPo1,len(listaP)):
                                    if (elementoNP == listaP[i]):
                                        elementoNP = elementoNP
                                    else:
                                        numPo2 = i
                                        break
                                break
                        numPo1 += 1
                        numPo2 += 1
                        if (numPo2 != (numPo1 + 1)):
                            numSPa = 1
                            numSPo1 = 0
                            numSPo2 = 0
                            for i in range(numPo1,numPo2):
                                if (numSPa == listaSP[i]):
                                    numSPa += 1
                            elementoNSP = int(input("¿En que SubPaso quiere agregar el SubSubPaso? [1-" + str(numSPa - 1) + "]\n"))
                            if (elementoNSP >= 1 and elementoNSP <= (numSPa - 1)):
                                for i in range (numPo1,numPo2):
                                    if (elementoNSP == listaSP[i]):
                                        numSPo1 = i
                                        for i in range (numSPo1,numPo2):
                                            if (elementoNSP == listaSP[i]):
                                                elementoNSP = elementoNSP
                                            else:
                                                numSPo2 = i
                                                break
                                        break
                                numSPo1 += 1
                                numSPo2 += 1
                                numSSPa = 1
                                numSSPo = 0
                                for i in range(numSPo1,numSPo2):
                                    if (numSSPa == listaSSP[i]):
                                        numSSPa += 1
                                if(menuAP == 1):
                                    elementoNSSP = numSSPa
                                else:
                                    elementoNSSP = int(input("¿En que posicion quiere agregar el SubSubPaso? [1-" + str(numSSPa) + "]\n"))
                                if (elementoNSSP >= 1 and elementoNSSP <= numSSPa):
                                    if (elementoNSSP == 1):
                                        numSSPo = numSPo1
                                    elif (elementoNSSP == numSSPa):
                                        numSSPo = numSPo2 - 1
                                    else:
                                        for i in range (numSPo1,numSPo2):
                                            if (elementoNSSP == listaSSP[i]):
                                                numSSPo = i
                                                break
                                    elementoT = str(input("Ingrese el texto del SubSubpaso\n"))
                                    listaP.insert(numSSPo, elementoNP)
                                    listaSP.insert(numSSPo, elementoNSP)
                                    listaSSP.insert(numSSPo, elementoNSSP)
                                    listaT.insert(numSSPo, elementoT)
                                    numRP = (numSSPo + 1)
                                    for i in range (numRP,numSPo2):
                                        txtN = (listaSSP[i] + 1)
                                        listaSSP.pop(i)
                                        listaSSP.insert(i, txtN)
                                else:
                                    print("Intente de nuevo")
                            else:
                                print("Intente de nuevo")
                        else:
                            print("No hay Subpasos donde poner SubSubpasos")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos donde poner SubSubpasos")
        except ValueError:
            print("Intente de nuevo")
        for i in range (0,len(listaP)):
            if (listaT[i] == 0):
                listaP.pop(i)
                listaSP.pop(i)
                listaSSP.pop(i)
                listaT.pop(i)
                break
    elif(menuAP == 3):
        print("")
    else:
        print("Intente de nuevo")

def Editar(opcE):
    try:
        menuE = int(input('''Seleccione la opcion deseada
    1. Editar
    2. Salir\n'''))
    except ValueError:
        menuE = 0
    if (menuE == 1):
        try:
            listaP.append(0)
            listaSP.append(0)
            listaSSP.append(0)
            listaT.append(0)
            if (opcE == 1):
                elementoW = input("Esta accion editara el Titulo del Protocolo \n¿Desea continuar?[si/#]\n")
                if (elementoW == 'si'):
                    elementoT = str(input("Ingrese el nuevo Titulo\n"))
                    Titulo.pop(0)
                    Titulo.append(elementoT)
            elif (opcE == 2):
                if (len(listaP) > 1):
                    numPa = 1
                    numPo = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿Que Paso desea Editar? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo = i
                                break
                        elementoW = input("Esta accion editara el Paso " + str(elementoNP) +"\n¿Desea continuar?[si/#]\n")
                        if (elementoW == 'si'):
                            elementoT = str(input("Ingrese el nuevo texto del Paso\n"))
                            listaT.pop(numPo)
                            listaT.insert(numPo, elementoT)
                            print("Paso editado exitosamente")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos que borrar")
            elif (opcE == 3):
                if (len(listaP) > 1):
                    numPa = 1
                    numPo1 = 0
                    numPo2 = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿En que Paso se ubica el SubPaso a Editar? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo1 = i
                                for i in range (numPo1,len(listaP)):
                                    if (elementoNP == listaP[i]):
                                        elementoNP = elementoNP
                                    else:
                                        numPo2 = i
                                        break
                                break
                        numPo1 += 1
                        numPo2 += 1
                        numSPa = 1
                        numSPo = 0
                        for i in range(numPo1,numPo2):
                            if (numSPa == listaSP[i]):
                                numSPa += 1
                        elementoNSP = int(input("¿Que SubPaso desea Editar? [1-" + str(numSPa - 1) + "]\n"))
                        if (elementoNSP >= 1 and elementoNSP <= (numSPa - 1)):
                            for i in range (numPo1,numPo2):
                                if (elementoNSP == listaSP[i]):
                                    numSPo = i
                                    break
                            elementoW = input("Esta accion editara el SubPaso " + str(elementoNSP) + " del Paso " + str(elementoNP) + "\n¿Desea continuar?[si/#]\n")
                            if (elementoW == 'si'):
                                elementoT = str(input("Ingrese el nuevo texto del SubPaso\n"))
                                listaT.pop(numSPo)
                                listaT.insert(numSPo, elementoT)
                                print("SubPaso editado exitosamente")
                        else:
                            print("Intente de nuevo")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos donde borrar Subpasos")
            elif (opcE == 4):
                if (len(listaP) > 0):
                    numPa = 1
                    numPo1 = 0
                    numPo2 = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿En que Paso se ubica el SubSubPaso a Editar? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo1 = i
                                for i in range (numPo1,len(listaP)):
                                    if (elementoNP == listaP[i]):
                                        elementoNP = elementoNP
                                    else:
                                        numPo2 = i
                                        break
                                break
                        numPo1 += 1
                        numPo2 += 1
                        if (numPo2 != (numPo1 + 1)):
                            numSPa = 1
                            numSPo1 = 0
                            numSPo2 = 0
                            for i in range(numPo1,numPo2):
                                if (numSPa == listaSP[i]):
                                    numSPa += 1
                            elementoNSP = int(input("¿En que SubPaso se ubica el SubSubPaso a Editar? [1-" + str(numSPa - 1) + "]\n"))
                            if (elementoNSP >= 1 and elementoNSP <= (numSPa - 1)):
                                for i in range (numPo1,numPo2):
                                    if (elementoNSP == listaSP[i]):
                                        numSPo1 = i
                                        for i in range (numSPo1,numPo2):
                                            if (elementoNSP == listaSP[i]):
                                                elementoNSP = elementoNSP
                                            else:
                                                numSPo2 = i
                                                break
                                        break
                                numSPo1 += 1
                                numSPo2 += 1
                                numSSPa = 1
                                numSSPo = 0
                                for i in range(numSPo1,numSPo2):
                                    if (numSSPa == listaSSP[i]):
                                        numSSPa += 1
                                elementoNSSP = int(input("¿Que SubSubPaso desea Editar? [1-" + str(numSSPa - 1) + "]\n"))
                                if (elementoNSSP >= 1 and elementoNSSP <= (numSSPa - 1)):
                                    for i in range (numSPo1,numSPo2):
                                        if (elementoNSSP == listaSSP[i]):
                                            numSSPo = i
                                            break
                                    elementoW = input("Esta accion editara el SubSubPaso " + str(elementoNSSP) + " del SubPaso " + str(elementoNSP) + " del Paso " + str(elementoNP) + "\n¿Desea continuar?[si/#]\n")
                                    if (elementoW == 'si'):
                                        elementoT = str(input("Ingrese el nuevo texto del SubSubPaso\n"))
                                        listaT.pop(numSSPo)
                                        listaT.insert(numSSPo, elementoT)
                                        print("SubSubPaso editado exitosamente")
                                else:
                                    print("Intente de nuevo")
                            else:
                                print("Intente de nuevo")
                        else:
                            print("No hay Subpasos donde Editar SubSubpasos")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos donde Editar SubSubpasos")
        except ValueError:
            print("Intente de nuevo")
        for i in range (0,len(listaP)):
            if (listaT[i] == 0):
                listaP.pop(i)
                listaSP.pop(i)
                listaSSP.pop(i)
                listaT.pop(i)
                break
    elif(menuE == 2):
        print("")
    else:
        print("Intente de nuevo")

def BorrarPaso(opcBP):
    try:
        menuBP = int(input('''Seleccione la opcion deseada
    1. Borrar
    2. Salir\n'''))
    except ValueError:
        menuBP = 0
    if (menuBP == 1):
        try:
            listaP.append(0)
            listaSP.append(0)
            listaSSP.append(0)
            listaT.append(0)
            if (opcBP == 1):
                if (len(listaP) > 1):
                    numPa = 1
                    numPo = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿Que Paso desea borrar? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo = i
                                break
                        elementoW = input("Esta accion tambien borrara Subpasos y SubSubpasos\n¿Desea continuar?[si/#]\n")
                        if (elementoW == 'si'):
                            numV = numPo
                            for i in range (numPo,len(listaP)):
                                i = numV
                                if(elementoNP == listaP[i]):
                                    listaP.pop(i)
                                    listaSP.pop(i)
                                    listaSSP.pop(i)
                                    listaT.pop(i)
                                    numV = i
                                else:
                                    txtN = (listaP[i] - 1)
                                    listaP.pop(i)
                                    listaP.insert(i, txtN)
                                    numV = i + 1
                            print("Paso eliminado exitosamente")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos que borrar")
            elif (opcBP == 2):
                if (len(listaP) > 1):
                    numPa = 1
                    numPo1 = 0
                    numPo2 = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿En que Paso se ubica el SubPaso a borrar? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo1 = i
                                for i in range (numPo1,len(listaP)):
                                    if (elementoNP == listaP[i]):
                                        elementoNP = elementoNP
                                    else:
                                        numPo2 = i
                                        break
                                break
                        numPo1 += 1
                        numPo2 += 1
                        numSPa = 1
                        numSPo = 0
                        for i in range(numPo1,numPo2):
                            if (numSPa == listaSP[i]):
                                numSPa += 1
                        elementoNSP = int(input("¿Que SubPaso desea borrar? [1-" + str(numSPa - 1) + "]\n"))
                        if (elementoNSP >= 1 and elementoNSP <= (numSPa - 1)):
                            for i in range (numPo1,numPo2):
                                if (elementoNSP == listaSP[i]):
                                    numSPo = i
                                    break
                            elementoW = input("Esta accion tambien borrara SubSubpasos\n¿Desea continuar?[si/#]\n")
                            if (elementoW == 'si'):
                                numV = numSPo
                                for i in range (numSPo,numPo2):
                                    i = numV
                                    if(elementoNSP == listaSP[i]):
                                        listaP.pop(i)
                                        listaSP.pop(i)
                                        listaSSP.pop(i)
                                        listaT.pop(i)
                                        numV = i
                                    else:
                                        txtN = (listaSP[i] - 1)
                                        listaSP.pop(i)
                                        listaSP.insert(i, txtN)
                                        numV = i + 1
                                print("SubPaso eliminado exitosamente")
                        else:
                            print("Intente de nuevo")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos donde borrar Subpasos")
            elif (opcBP == 3):
                if (len(listaP) > 0):
                    numPa = 1
                    numPo1 = 0
                    numPo2 = 0
                    for i in range(0,len(listaP)):
                        if (numPa == listaP[i]):
                            numPa += 1
                    elementoNP = int(input("¿En que Paso se ubica el SubSubPaso a borrar? [1-" + str(numPa - 1) + "]\n"))
                    if (elementoNP >= 1 and elementoNP <= (numPa - 1)):
                        for i in range (0,len(listaP)):
                            if (elementoNP == listaP[i]):
                                numPo1 = i
                                for i in range (numPo1,len(listaP)):
                                    if (elementoNP == listaP[i]):
                                        elementoNP = elementoNP
                                    else:
                                        numPo2 = i
                                        break
                                break
                        numPo1 += 1
                        numPo2 += 1
                        if (numPo2 != (numPo1 + 1)):
                            numSPa = 1
                            numSPo1 = 0
                            numSPo2 = 0
                            for i in range(numPo1,numPo2):
                                if (numSPa == listaSP[i]):
                                    numSPa += 1
                            elementoNSP = int(input("¿En que SubPaso se ubica el SubSubPaso a borrar? [1-" + str(numSPa - 1) + "]\n"))
                            if (elementoNSP >= 1 and elementoNSP <= (numSPa - 1)):
                                for i in range (numPo1,numPo2):
                                    if (elementoNSP == listaSP[i]):
                                        numSPo1 = i
                                        for i in range (numSPo1,numPo2):
                                            if (elementoNSP == listaSP[i]):
                                                elementoNSP = elementoNSP
                                            else:
                                                numSPo2 = i
                                                break
                                        break
                                numSPo1 += 1
                                numSPo2 += 1
                                numSSPa = 1
                                numSSPo = 0
                                for i in range(numSPo1,numSPo2):
                                    if (numSSPa == listaSSP[i]):
                                        numSSPa += 1
                                elementoNSSP = int(input("¿Que SubSubPaso desea borrar? [1-" + str(numSSPa - 1) + "]\n"))
                                if (elementoNSSP >= 1 and elementoNSSP <= (numSSPa - 1)):
                                    for i in range (numSPo1,numSPo2):
                                        if (elementoNSSP == listaSSP[i]):
                                            numSSPo = i
                                            break
                                    elementoW = input("¿Desea continuar en la eliminacion?[si/#]\n")
                                    if (elementoW == 'si'):
                                        numV = numSSPo
                                        for i in range (numSSPo,numSPo2):
                                            i = numV
                                            if(elementoNSSP == listaSSP[i]):
                                                listaP.pop(i)
                                                listaSP.pop(i)
                                                listaSSP.pop(i)
                                                listaT.pop(i)
                                                numV = i
                                            else:
                                                txtN = (listaSSP[i] - 1)
                                                listaSSP.pop(i)
                                                listaSSP.insert(i, txtN)
                                                numV = i + i
                                        print("SubSubPaso eliminado exitosamente")
                                else:
                                    print("Intente de nuevo")
                            else:
                                print("Intente de nuevo")
                        else:
                            print("No hay Subpasos donde borrar SubSubpasos")
                    else:
                        print("Intente de nuevo")
                else:
                    print("No hay pasos donde borrar SubSubpasos")
        except ValueError:
            print("Intente de nuevo")
        for i in range (0,len(listaP)):
            if (listaT[i] == 0):
                listaP.pop(i)
                listaSP.pop(i)
                listaSSP.pop(i)
                listaT.pop(i)
                break
    elif(menuBP == 2):
        print("")
    else:
        print("Intente de nuevo")
        
def MostrarProtocolo():
    print("\n" + str(Titulo[0]) + "\n")
    for i in range (0, len(listaP)):
        if (listaSSP[i] == 0):
            if (listaSP[i] == 0):
                print(str(listaP[i]) + ".- " + str(listaT[i]))
            else:
                print(str(listaP[i]) + "." + str(listaSP[i]) + ".- " + str(listaT[i]))
        else:
            print(str(listaP[i]) + "." + str(listaSP[i]) + "." + str(listaSSP[i]) + ".- " + str(listaT[i]))
    print(listaP)
    print(listaSP)
    print(listaSSP)
    print(listaT)

print("Programa para hacer un Protocolo")
elementoTi = str(input("Ingrese el Titulo del protocolo\n"))
Titulo.append(elementoTi)
p = 1
while (p == 1):
    try:
        menu = int(input ('''
    Seleccione la opción deseada:
    1. Agregar
    2. Editar
    3. Borrar
    4. Mostrar Protocolo
    5. Salir del Programa\n'''))
    except ValueError:
        menu = 0
    if (menu == 1):
        p1 = 1
        while (p1 == 1):
            try:
                opc = int(input('''\nSeleccione que desea agregar
    1. Paso
    2. SubPaso
    3. SubSubPaso\n'''))
                if opc == 1:
                    AñadirPaso(1)
                elif opc == 2:
                    AñadirPaso(2)
                elif opc == 3:
                    AñadirPaso(3)
                else:
                    print ("Intente de nuevo")
            except ValueError:
                print("Intente de nuevo")
            con = str(input("¿Quiere agregar otro Paso?\nIntroduzca si para continuar\n"))
            if con == 'si':
                p1 = 1
            else:
                p1 = 2
    elif (menu == 2):
        p2 = 1
        while (p2 == 1):
            try:
                opc = int(input('''\nSeleccione que desea editar
    1. Tituló
    2. Paso
    3. SubPaso
    4. SubSubPaso\n'''))
                if opc == 1:
                    Editar(1)
                elif opc == 2:
                    Editar(2)
                elif opc == 3:
                    Editar(3)
                elif opc == 4:
                    Editar(4)
                else:
                    print ("Intente de nuevo")
            except ValueError:
                print("Intente de nuevo")
            con = str(input("¿Quiere editar otro Elemento?\nIntroduzca si para continuar\n"))
            if con == 'si':
                p2 = 1
            else:
                p2 = 2
    elif (menu == 3):
        p3 = 1
        while (p3 == 1):
            try:
                opc = int(input('''\nSeleccione que desea borrar
    1. Paso
    2. SubPaso
    3. SubSubPaso\n'''))
                if opc == 1:
                    BorrarPaso(1)
                elif opc == 2:
                    BorrarPaso(2)
                elif opc == 3:
                    BorrarPaso(3)
                else:
                    print ("Intente de nuevo")
            except ValueError:
                print("Intente de nuevo")
            con = str(input("¿Quiere borrar otro Paso?\nIntroduzca si para continuar\n"))
            if con == 'si':
                p3 = 1
            else:
                p3 = 2
    elif (menu == 4):
        MostrarProtocolo()
    elif (menu == 5):
        p = 2
    else:
        p = 1
