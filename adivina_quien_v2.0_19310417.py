"""
***ADIVINA QUIÉN ***
***    ver 2     ***
@author: Cristian Villaseñor
"""
#En esta versión no se maneja el aprendizaje 
#pero auto-selecciona la mejor pregunta y se implementa base de datos

import mysql.connector
import random

preguntas=["¿Es hombre?",
           "¿Tiene el pelo largo?",
           "¿Tiene barba/bigote?",
           "¿Se llama Daniel?",
           "¿Su registro comienza con 19110...?",
           "¿Tiene el pelo chino?",
           "¿Usa lentes?",
           "¿Tiene el pelo Negro o castaño?",
           "¿Se llama Juan?",
           "¿Tiene complexión delgada?" ]

respuestas=[5,5,5,5,5,5,5,5,5,5]
#---------------------------------------
def buscapregunta(datos):
    unos=[0,0,0,0,0,0,0,0,0,0]
    ceros=[0,0,0,0,0,0,0,0,0,0]
    mindif=50
    colum=0
    for x in range(2,12):
        for y in range(len(datos)):
            if(datos[y][x]==1):
                unos[x-2]=unos[x-2]+1
            if(datos[y][x]==0):
                ceros[x-2]=ceros[x-2]+1
        dif=abs(unos[x-2]-ceros[x-2])
        if(dif<mindif):
            mindif=dif
            colum=x
    return colum-2
#---------------------------------------
def remuevedatos(datos,columna,resp):
    x = columna+2
    bandera=0
    y=0
    while (bandera==0):
       if(datos[y][x]!=resp):
           datos.pop(y)
       else:
           y=y+1
       if(y>=len(datos)): bandera=1
#---------------------------------------   
def datousuario(columna,modo):
    bandera=0
    while(bandera==0):
        resp=int(input()) 
        if(resp != 0 and resp!= 1):
            print("Respuesta invalida intentalo de nuevo")
            if(modo==0): print(preguntas[columna])
            else:        print("¿acerté?\nIngresa tu respuesta 1 para si y 0 para no")
        else: bandera=1
    return resp
#---------------------------------------
reinicio=0
while(reinicio==0):
    cnn = mysql.connector.connect(host="localhost", user="root",
                                  passwd="cris2000", database="adivina7F1")

    cur = cnn.cursor()
    cur.execute("SELECT * FROM alumnos")
    datos = cur.fetchall()
    
    print("Bienvenido al sistema de Adivina Quien del 7F1\n\nPiensa en un compañero del salón y yo intentaré adivinarlo\n")
    for etapa in range(5):
        columna = buscapregunta(datos)
        print(preguntas[columna])
        print("Ingresa tu respuesta 1 para si y 0 para no")
        respuestas[columna]=datousuario(columna,0)
        remuevedatos(datos, columna, respuestas[columna])
    
        if(len(datos)==1):
            print("¡Ya sé! Estas pensando en ",datos[0][1], "¿acerté?")
            print("Ingresa tu respuesta 1 para si y 0 para no")
            final=datousuario(0,1)
            break
        
    if(len(datos)>1):
        print("Hmmm hay mas de una persona con esa descripción....\n")
        azar=random.randint(0,len(datos)-1)
        print("¡Ya sé! Estas pensando en ",datos[azar][1], "¿acerté?")
        print("Ingresa tu respuesta 1 para si y 0 para no")
        final=datousuario(0,1)

    if(final == 1): print("Yo siempre gano, gracias por jugar")
    else: print("Vaya creo que debo de afinar mis habilidades de adivinación")
    reinicio=1
    print("Si deseas volver a jugar presiona 1 de lo contrario presiona 0")
    inicio=datousuario(0,1)
    if(inicio ==1):
        print("\nReinciando....\n\n\n")
        reinicio=0
        respuestas=[5,5,5,5,5,5,5,5,5,5]
    else:
        print("\nHasta luego....")
        cur.close()
        cnn.close()
        