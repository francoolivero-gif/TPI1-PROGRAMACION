def vectores():
    vec1=[101,102,103,104,105,106]
    vec2=[104,105,106,107,108]
    vec3=[102,105,109]
    return vec1,vec2,vec3
def interseccion(v1,v2):
    vector_interseccion=[]
    for i in range(len(v2)):
        for j in range(len(v1)):
            if v2[i] == v1[j]:
                vector_interseccion.append(v2[i])
    print('Los usuarios que utilizan ambas plataformas son: ',vector_interseccion)
    return vector_interseccion
def union(v1,v2):
    vec4=[]
    vec5=[]
    vec6=[]
    vec7=[]
    vector_union=[]
    for i in range(len(v1)):
        for j in range(len(v2)):
            if v1[i]==v2[j]:
                vec5.append(v1[i])
    for i in range(len(v1)):
        encontrado=False
        for j in range(len(vec5)):
            if v1[i]==vec5[j]:
                encontrado=True
                break
        if encontrado==False:
            vec4.append(v1[i])
            vec6=vec4+vec5
    for i in range(len(v2)):
        encontrado=False
        for j in range(len(vec6)):
            if v2[i]==vec6[j]:
                encontrado=True
                break
        if encontrado==False:
            vec7.append(v2[i])
            vector_union=vec6+vec7
    print('Los usuarios que utilizan al menos una plataforma son:', vector_union)
    return vector_union 
def sin_errores(v3,vector_union):
    vector4=[]
    for i in range(len(vector_union)):
        encontrado=False
        for j in range(len(v3)):
            if vector_union[i]==v3[j]:
                encontrado=True
                break
        if encontrado==False:
            vector4.append(vector_union[i])
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
v1,v2,v3=vectores()   
vector_interseccion=interseccion(v1,v2)
vector_union=union(v1,v2)
sin_errores(v3,vector_union)
una_plataforma(vector_interseccion,vector_union)



