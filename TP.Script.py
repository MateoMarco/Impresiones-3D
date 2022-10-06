def texto_lista(txt):
    txt += '.txt'
    archivoR = open(txt, 'r')
    lista = []
    archivoR.readline().rstrip() #Se saltea el titulo
    linea = archivoR.readline().rstrip()
    while linea != '':
        lista.append(linea)
        linea = archivoR.readline().rstrip()
    
    return lista

#AGREGADO
def matriz_cero (cf, cc):
    
    """Poner la matriz con sus respectivos 0"""
    matriz = []
    for i in range (cf):
        matriz.append ( [0] * cc )
    return matriz


def matriz_asociada (cf,cc,matriz,archivo):
    
    """Llenar una matriz que antes tenia 0s con los datos de filas y columnas"""
    
    archivoR = open ( archivo , "r")
    for i in range (cf):
        archivoR.readline()
        for j in range (cc):
            dato = int(archivoR.readline())
            matriz [i][j] = dato
        
    archivoR.close()
    
    return matriz

  #Funcion para obtener una tabla
def tabla (cf, cc, filaprincipal, columnaprincipal, mensaje, encabezado, matriz):

    print (f"\nTabla de {mensaje}:")
    print ("\n")
    
    #Estructura de tabla
    
    print (f"{encabezado}".rjust(10) , end="")
    
    for j in range (cc):
        print ( filaprincipal[j].rjust(10) , end="")
    print ("\n")
    
    for i in range (cf):
        print ( columnaprincipal[i].rjust(10) , end="")
        
        for j in range (cc):
            print (str(matriz[i][j]).rjust(10) , end="") #Lo paso a str porque son datos numericos
        print ("\n")

def suma_filas(matriz, cf, cc):
    filas = []
    for i in range(cf):
        suma = 0
        for j in range(cc):
            suma += matriz[i][j]
        filas.append(suma)
    return filas

def orden_insercion(lista1,lista2):
    for i in range(1,len(lista1)):
        aux = lista1[i]
        aux2 = lista2[i]
        
        j = i - 1
        while j >= 0 and aux > lista1[j]:
            lista1[j+1] = lista1[j]
            lista2[j+1] = lista2[j]
            j = j - 1
        
        lista1[j+1] = aux
        lista2[j+1] = aux2
        
def maximo_matriz(matriz,cf,cc):
    max = matriz[0][0]
    pi = []
    pj = []
    
    for i in range(cf):
        for j in range(cc):
            if matriz[i][j] > max:
                max = matriz[i][j]
                pi = []
                pj = []
                pi.append(i)
                pj.append(j)
                
            elif matriz[i][j] == max:
                pi.append(i)
                pj.append(j)
                
    return max, pi, pj

def texto_2listas(txt):
    txt += '.txt'
    archivoR = open(txt, 'r')
    lista1 = []
    lista2 = []
    archivoR.readline().rstrip() #Se saltea el titulo
    linea = archivoR.readline().rstrip()
    while linea != '':
        lista1.append(float(archivoR.readline()))
        lista2.append(float(archivoR.readline()))
        linea = archivoR.readline().rstrip()
    
    return lista1, lista2


def busbin(k, lista):
    i = 0
    s = len(lista) - 1
    pm = (i + s) // 2
    while i <= s and lista[pm] != k:
        if k > lista[pm]:
            i = pm + 1
        else: s = pm - 1
        
        pm = (i + s) // 2
    
    if i > s: pm = -1
    return pm

def calc_cant ( dens , pesorollo , vol , cant ):
    
    #Calculo de cantidad de rollos y gramos de filamento, con el peso en gr, el volumen en cm3
    
    grfil= dens*vol*cant
    rollos= grfil/pesorollo
    
    return grfil, rollos

#AGR    
            

def principal():
    materiales = texto_lista ("materiales")
    materiales.sort()
    meses = texto_lista("meses")
    densidad, precios = texto_2listas("densidadyprecios")
    
      
    cf = len(materiales)
    cc = len(meses)
            
    consumo = "consumo.txt"
    matrizvacia = matriz_cero ( cf , cc ) #Creo la matriz pero con 0s
    matrizcargada = matriz_asociada ( cf , cc , matrizvacia , consumo ) #Lleno con los datos la matriz vacia
    
    #Menu Principal
    comando = '0'
    while comando != '5':
        print("""
    1 - Mostrar listado de materiales y meses a procesar
    2 - Mostrar consumo de filamentos
    3 - Mostrar consumo total de cada material y maximo consumo
    4 - Presupuestos y Actualizacion del consumo
    5 - Salir del programa\n""")
        
        comando = input('Seleccione una opcion: ')
              
        if comando == '1':
            print('\nLos materiales disponibles son:\n')
            for i in materiales:
                print(i)
            print('\nLos meses a procesar son:\n')
            for i in meses:
                print(i)
                
        elif comando == "2":
                    
            
            
            tabla_de = "Consumo de material, acorde a cada mes"
            
            tablaconsumo = tabla ( cf, cc, meses, materiales, tabla_de, "Consumo" , matrizcargada) #Utilizo la funcion de tabla previamente introducida
        
        
        elif comando == '3':    
            
            subcomando = input('''

        Seleccione una opcion:
            
        1 - Ver consumo total de cada material en el semestre
        2 - Ver mayor consumo del semestre (material y mes)
        3 - Volver al menu principal''')
    
            
            # UN SUBMENÚ REQUIERE DE UN CICLO WHILE QUE PERMITA VOLVER AL SUBMENÚ Y DAR UNA OPCIÓN DE SALIDA
            
            while subcomando != '3':
                if subcomando == '1':
                
                    consumo_semestre = suma_filas(matrizcargada, cf,cc)
                    copiaconsumo = consumo_semestre.copy()
                    copiamateriales = materiales.copy()
                    orden_insercion(copiaconsumo, copiamateriales)
                
                    print ('\nEl consumo total de filamentos en el semestre de cada material fue: \n')
                    for i in range(0,len(copiaconsumo)):
                        print(copiamateriales[i].rjust(6), str(copiaconsumo[i]).rjust(15))
                        
                elif subcomando == '2': # <-- ES ELIF (NO IF EN SECUENCIA)
                    
                    max, pi, pj = maximo_matriz(matrizcargada, cf, cc)
                    
                    print('El mayor consumo de filamento registrado fue de:', max, '\ny corresponde a:\n')
                    for x in range (0,len(pi)):
                        i = pi[x]
                        j = pj[x]
                        print(materiales[i].rjust(6), meses[j].upper().rjust(10))
                
                subcomando = input('''

        Seleccione una opcion:
            
        1 - Ver consumo total de cada material en el semestre
        2 - Ver mayor consumo del semestre (material y mes)
        3 - Volver al menu principal''')
                
        
        elif comando == '4':
            
            print(matrizcargada)
            presupuesto = input ('Ingrese el numero de presupuesto (0 para terminar)')
            while presupuesto != '0':
                nombre = input('Nombre de la pieza: ')
                material = input('Material: ').upper()
                pm = busbin(material.upper(), materiales)
                while pm == -1:
                    material = input('Material inexistente. Ingrese otro material: ')
                    pm = busbin(material, materiales)
                volumen = float(input('Volumen: '))
                unidades = int(input('Cantidad de unidades: '))
                
                grfil, rollos = calc_cant(densidad[pm], 750, volumen, unidades)
                
                matrizcargada[pm][5] += rollos
                
                presupuesto = input ('Ingrese el numero de presupuesto (0 para terminar)')
                
            print(matrizcargada)
                
        input('\n\n\nPresione Enter para volver al menu principal') 


principal()
