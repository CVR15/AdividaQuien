"""
***ADIVINA QUIÉN ***
***    ver 1     ***
@author: Cristian Villaseñor
"""
#En esta versión no se maneja el aprendizaje aún
#Modelo base de if-else 
bandera = 0
preg=['\0','\0','\0','\0','\0','\0']
reinicio=0
while (reinicio==0):
    print("Bienvenido al sistema de Adivina Quien del 7F1\n\nPiensa en un compañero del salón y yo intentaré adivinarlo")
    while(bandera ==0):
        print("1. ¿Es hombre?\ns/n")
        preg[0]=input()
        if (preg[0] != 's' and preg[0] != 'n'):  print("Respuesta invalida intentalo de nuevo")
        else: bandera=1
        
    while(bandera ==1):
        if (preg[0] == 'n'):   
            print("2. ¿Actualmente tiene el pelo negro o castaño? \ns/n")
            preg[1]=input()           
        if (preg[0] == 's'):   
            print("2. ¿Tiene barba/bigote?\ns/n")
            preg[1]=input()
                    
        if (preg[1] != 's' and preg[1] != 'n'):  print("Respuesta invalida intentalo de nuevo")
        else: bandera=2
                    
    while(bandera ==2):
        if (preg[0] == 'n' and preg[1] == 'n'):   
            print("3. ¿Es de estatura media-baja? \ns/n")
            preg[2]=input()                            
        if (preg[0] == 'n' and preg[1] == 's'):  
            print("3. ¿Tiene el pelo chino? \ns/n")
            preg[2]=input()    
        if (preg[0] == 's' and preg[1] == 'n'):  
            print("3. ¿Es muy delgad@? \ns/n")
            preg[2]=input()    
        if (preg[0] == 's' and preg[1] == 's'):  
            print("3. ¿Su registro empieza con 19110... ? \ns/n")
            preg[2]=input()
    
        if (preg[2] != 's' and preg[2] != 'n'):  print("Respuesta invalida intentalo de nuevo")
        else: bandera=3
    
    while(bandera ==3):
        if (preg[0] == 'n' and preg[1] == 'n' and preg[2] == 'n'):   
            print("¡Ya sé! Estas pensando en Yadira, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[0] == 'n' and preg[1] == 'n' and preg[2] == 's'):   
            print("¡Ya sé! Estas pensando en Rosario, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[0] == 'n' and preg[1] == 's' and preg[2] == 'n'):   
            print("¡Ya sé! Estas pensando en Estefany, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[0] == 'n' and preg[1] == 's' and preg[2] == 's'):   
            print("¡Ya sé! Estas pensando en Monica, ¿Acerté?\ns/n")
            preg[5]=input()
    
        if (preg[0] == 'n' and preg[5] != 's' and preg[5] != 'n'):  print("Respuesta invalida intentalo de nuevo")
        else: 
            bandera=6
            reinicio=1
                
        if (preg[0] == 's' and preg[1] == 'n' and preg[2] == 'n'):   
            print("4. ¿Tiene el pelo chino? \ns/n")
            preg[3]=input() 
        if (preg[0] == 's' and preg[1] == 'n' and preg[2] == 's'):   
             print("4. ¿Se llama Juan? \ns/n")
             preg[3]=input()
        if (preg[0] == 's' and preg[1] == 's' and preg[2] == 'n'):   
            print("4. ¿Es muy delgad@? \ns/n")
            preg[3]=input() 
        if (preg[0] == 's' and preg[1] == 's' and preg[2] == 's'):   
             print("4. ¿Se llama Daniel? \ns/n")
             preg[3]=input()    
        
        if (preg[0] == 's'):
            if(preg[3] != 's' and preg[3] != 'n'):  print("Respuesta invalida intentalo de nuevo")
            else: bandera=4

    while(bandera ==4):
        if (preg[1] == 'n' and preg[2] == 'n' and preg[3] == 'n'):   
            print("5. ¿Usa lentes? \ns/n")
            preg[4]=input()
        if (preg[1] == 'n' and preg[2] == 'n' and preg[3] == 's'):   
            print("5. Se llama Daniel? \ns/n")
            preg[4]=input()
        if (preg[1] == 'n' and preg[2] == 's' and preg[3] == 'n'):   
            print("¡Ya sé! Estas pensando en Andrés Rosales, ¿Acerté?\ns/n")
            preg[5]=input()
            if (preg[5] != 's' and preg[5] != 'n'):  print("Respuesta invalida intentalo de nuevo")
            else: 
                bandera=6
                reinicio=1
        if (preg[1] == 'n' and preg[2] == 's' and preg[3] == 's'):   
            print("¡Ya sé! Estas pensando en Juan Israel, ¿Acerté?\ns/n")
            preg[5]=input()
            if (preg[5] != 's' and preg[5] != 'n'):  print("Respuesta invalida intentalo de nuevo")
            else: 
                bandera=6
                reinicio=1
        if (preg[1] == 's' and preg[2] == 'n' and preg[3] == 'n'):   
            print("5. ¿Usa lentes? \ns/n")
            preg[4]=input()
        if (preg[1] == 's' and preg[2] == 'n' and preg[3] == 's'):   
            print("5. ¿Se llama Daniel? \ns/n")
            preg[4]=input()
        if (preg[1] == 's' and preg[2] == 's' and preg[3] == 'n'):   
            print("5. ¿Es muy delgado? \ns/n")
            preg[4]=input()
        if (preg[1] == 's' and preg[2] == 's' and preg[3] == 's'):
            print("5. ¿Usa lentes? \ns/n")
            preg[4]=input()
        
        if((preg[1]=='s')or(preg[2]=='n')):
           if(preg[4] != 's' and preg[4] != 'n'):  print("Respuesta invalida intentalo de nuevo")
           else: bandera=5
           
    while(bandera==5):
        if (preg[1] == 'n' and preg[2] == 'n' and preg[3] == 'n' and preg[4] == 'n'):   
            print("¡Ya sé! Estas pensando en Ricardo, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 'n' and preg[2] == 'n' and preg[3] == 'n' and preg[4] == 's'):   
            print("¡Ya sé! Estas pensando en Eliseo, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 'n' and preg[2] == 'n' and preg[3] == 's' and preg[4] == 'n'):   
            print("¡Ya sé! Estas pensando en Enrique, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 'n' and preg[2] == 'n' and preg[3] == 's' and preg[4] == 's'):   
            print("¡Ya sé! Estas pensando en Daniel Panes, ¿Acerté?\ns/n")
            preg[5]=input()
            
        if (preg[1] == 's' and preg[2] == 'n' and preg[3] == 'n' and preg[4] == 'n'):   
            print("¡Ya sé! Estas pensando en Juan Pablo, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 's' and preg[2] == 'n' and preg[3] == 'n' and preg[4] == 's'):   
            print("¡Ya sé! Estas pensando en Cristian, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 's' and preg[2] == 'n' and preg[3] == 's' and preg[4] == 'n'):   
            print("¡Ya sé! Estas pensando en Josue, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 's' and preg[2] == 'n' and preg[3] == 's' and preg[4] == 's'):   
            print("¡Ya sé! Estas pensando en Omar Daniel, ¿Acerté?\ns/n")
            preg[5]=input()
              
        if (preg[1] == 's' and preg[2] == 's' and preg[3] == 'n' and preg[4] == 'n'):   
            print("¡Ya sé! Estas pensando en Javier, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 's' and preg[2] == 's' and preg[3] == 'n' and preg[4] == 's'):   
            print("¡Ya sé! Estas pensando en MAximiliano, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 's' and preg[2] == 's' and preg[3] == 's' and preg[4] == 'n'):   
            print("¡Ya sé! Estas pensando en Daniel Pelayo, ¿Acerté?\ns/n")
            preg[5]=input()
        if (preg[1] == 's' and preg[2] == 's' and preg[3] == 's' and preg[4] == 's'):   
            print("¡Ya sé! Estas pensando en Luis Daniel, ¿Acerté?\ns/n")
            preg[5]=input()  
            
        
        if (preg[5] != 's' and preg[5] != 'n'):  print("Respuesta invalida intentalo de nuevo")
        else: 
            bandera=6
            reinicio=1
            
    if(preg[5] == 's'): print("Yo siempre gano, gracias por jugar")
    else: print("Vaya creo que debo de afinar mis habilidades de adivinación")
    print("Si deseas volver a jugar presiona s")
    inicio=input()
    if(inicio =='s'):
        print("\nReinciando....\n\n\n")
        reinicio=0
        bandera=0
        preg=['\0','\0','\0','\0','\0','\0']
    else:
        print("\nHasta luego....")

