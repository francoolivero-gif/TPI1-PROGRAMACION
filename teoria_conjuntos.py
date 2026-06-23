from datetime import datetime
def menu():
    path="C:\logs\logs.txt"
    try:
        arch_trazas = open(path, "a")
    except FileNotFoundError:
        print("La ruta no existe.")
    conjunto1=[101,102,103,104,105,106]
    conjunto2=[104,105,106,107,108]
    conjunto3=[102,105,109]

    while True:
        print("1. Mostrar Ejercicio 1")
        print("2. Mostrar Ejercicio 3")
        print("3. Salir")
        opcion = int(input("Ingrese que opcion desea elegir: "))
        if opcion == 1:
            print("1. Mostrar Punto A")
            print("2. Mostrar Punto B")
            arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

            opcion2 = int(input("Ingrese que opcion desea elegir: "))

            if opcion2 == 1:
                print("1. Mostrar Union Conjunto 1 y 2")
                print("2. Mostrar Interseccion Conjunto 1 y 2")
                print("3. Mostrar los que no tienen errores")
                print("4. Mostrar los que usan tan solo 1 plataforma")
                arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion2) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

                
                opcion3 = int(input("Elige que opcion desea elegir: "))
                if opcion3 == 1:
                    union(conjunto1,conjunto2)
                    arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion3) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

                elif opcion3 == 2:
                    interseccion(conjunto1,conjunto2)
                    arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion3) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

                elif opcion3 == 3:
                    sin_errores(conjunto1, conjunto2, conjunto3)
                    arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion3) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")
                elif opcion3 == 4:
                    una_plataforma(conjunto1,conjunto2,conjunto3)
                    arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion3) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")
                else:
                    print("El numero ingresado no es una opcion disponible.")
                    arch_trazas.writelines("el usuario ingreso una opcion incorrecta" + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

            elif opcion2 == 2:
                tabla_verdad(conjunto1,conjunto2,conjunto3)
                arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion2) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")
            else:
                print("El numero ingresado no es una opcion disponible.")
                arch_trazas.writelines("el usuario ingreso una opcion incorrecta" + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

        
        elif opcion == 2:
            ejercicio3()
            arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")
            
        elif opcion == 3:
            print("Saliendo del sistema...")
            arch_trazas.writelines("Se ejecuto la opcion: "+ str(opcion) + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")
            break
        else:
            print("El numero ingresado no es una opcion disponible.")
            arch_trazas.writelines("el usuario ingreso una opcion incorrecta" + " " + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")

def interseccion(conjunto1,conjunto2): #funcion para saber los usarios que uitlizan ambas plataformas 
    vector_interseccion=[]
    for i in range(len(conjunto2)):
        for j in range(len(conjunto1)):
            if conjunto2[i] == conjunto1[j]:
                vector_interseccion.append(conjunto2[i])
    print('Los usuarios que utilizan ambas plataformas son: ',vector_interseccion)

def union(conjunto1,conjunto2): #funcion para saber que usarios usan la API Y WEB
    conjuntounion = conjunto1
    for i in range(len(conjunto2)):
        controlador = 0
        for j in range(len(conjuntounion)): 
            if conjunto2[i] == conjuntounion[j]:
                controlador += 1
        if controlador == 0:
            conjuntounion.append(conjunto2[i])
    print(f"La union del Conjunto A con el Conjunto B es: A U B = {conjuntounion}")

def sin_errores(conjunto1, conjunto2, conjunto3):
    conjuntounion = conjunto1
    for i in range(len(conjunto2)):
        controlador = 0
        for j in range(len(conjuntounion)): 
            if conjunto2[i] == conjuntounion[j]:
                controlador += 1
        if controlador == 0:
            conjuntounion.append(conjunto2[i])

    vector4=[]
    for i in range(len(conjuntounion)):
        encontrado=False
        for j in range(len(conjunto3)):
            if conjuntounion[i]==conjunto3[j]:
                encontrado=True
                break
        if encontrado==False:
            vector4.append(conjuntounion[i])
    print('Los usuarios que no tienen errores son: ',vector4)
def una_plataforma(vector_interseccion,vector_union):
    vector_una_plataforma=[]
    for i in range(len(vector_union)):
        encontrado=False
        for j in range(len(vector_interseccion)):
            if vector_union[i]==vector_interseccion[j]:
                encontrado=True
                break
        if encontrado==False:
            vector_una_plataforma.append(vector_union[i])
    print('Los usuarios que usan una sola plataforma son: ',vector_una_plataforma)

def tabla_verdad(conjunto1,conjunto2,conjunto3):

    p = conjunto1
    q = conjunto2
    r = conjunto3
    
    criticos = []
    no_criticos = []

    # UNIR CONJUNTO 1 CON 2 (YA QUE LA FUNCION ERA: NO CRITICOS = (P O R) Y R
    conjuntounion = []
    for i in range(len(p)):
        conjuntounion.append(p[i])
    
    for i in range(len(q)):
        controlador = 0
        for j in range(len(conjuntounion)): 
            if q[i] == conjuntounion[j]:
                controlador += 1
        if controlador == 0:
            conjuntounion.append(q[i])  
    
    # UBICAR ELEMENTOS EN CRITICOS O NO CRITICOS
    for i in range(len(conjuntounion)):
        controlador_critico = 0
        
        for j in range(len(r)):
            if conjuntounion[i] == r[j]:
                controlador_critico += 1
                
        if controlador_critico > 0:
            criticos.append(conjuntounion[i])
        if controlador_critico == 0:
            no_criticos.append(conjuntounion[i])
    
    # VERIFICAR SI EN R QUEDO ALGUN VALOR SIN UBICAR
    for i in range(len(r)):
        controlador_clasificado = 0
        for j in range(len(criticos)):
            if r[i] == criticos[j]:
                controlador_clasificado += 1
        
        if controlador_clasificado == 0:
            no_criticos.append(r[i])
            
    print("RESULTADOS DE LA CLASIFICACIÓN:")
    print(f"Usuarios Críticos: {criticos}")
    print(f"Usuarios No Críticos: {no_criticos}")
    
def ejercicio3():
    m=[
    [120,150,100],
    [200,180,220],
    [90,110,95]
    ]
    f1=0
    f2=0
    f3=0
    s1=0
    s2=0
    s3=0
    for i in range(len(m)):
            f1+=m[i][0]
            f2+=m[i][1]
            f3+=m[i][2]
    promedio1=f1/3
    promedio2=f2/3
    promedio3=f3/3
    print('el tiempo promedio de la primer funcion es',promedio1)
    print('el tiempo promedio de la segunda funcion es',promedio2)
    print('el tiempo promedio de la tercer funcion es',promedio3)
    for i in range(len(m)):
        s1+=m[0][i]
        s2+=m[1][i]
        s3+=m[2][i]
    promedioa=s1/3
    promediob=s2/3
    promedioc=s3/3
    print('el tiempo promedio del primer servidor es',promedioa)
    print('el tiempo promedio del segundo servidor es',promediob)
    print('el tiempo promedio del tercer servidor es',promedioc)
    
menu()
