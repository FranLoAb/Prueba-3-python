import json


#JSON
json = 'biblioteca.json'
autores = 'AutorID'
Nombre = 'Nombre'
Nacionalidad = 'Nacionalidad'
Categoria = 'CategoriaID'

def Reportes()
    

def AgregarAutor():      
    {
        "AutorID":  id[len] +1,
        "Nombre": input('ingrese nombre de autor: '),
        "Nacionalidad": input('Ingrese nacionalidad del autor: ')

        }
    autores.append(AgregarAutor)
        
    
#Write
def EditarAutor():
       with open (autores.load,'w') as file:
    
         Nacionalidad= int(input('ingrese la ID del autor'))
         autores = input('ingrese nombre del autor')
     


          
#Delete
def EliminarAutor():
    with open(autores.load,'w') as file:
         for autores in 'biblioteca.json':
             
         {
            "AutorID": int(input("Ingrese ID de autor a eliminar"))
             if 'AutorID' == 
             
         }

        




#Read   
def BuscarAutor(): 
    with open (autores.load,'r') as file:
     for autores in   json:
         json.load (file)


    

#Primer menú

while True:
    try:
        print('***M E N Ú***')
        print()
        print('1) Mantenedor de autores')
        print('2) Reportes')
        print('3) Salir')
        opciones = int(input("Seleccione una opción: "))
        

        #opciones menú

        if opciones == 1:

            #Segundo menú(mantenedor)
            while True:
                try:

                    print('***************************')
                    print('  MANTENEDOR DE AUTORES    ')
                    print('***************************')
                    print()
                    print('1] Agregar autor')
                    print('2] Editar autor')
                    print('3] Eliminar Autor')
                    print('4] Buscar autor')
                    print('5] Salir')
                    opcion = int(input('Seleccione una opción: '))

                    if opcion == 1:
                        AgregarAutor()

                    elif opcion == 2:
                        EditarAutor()

                    elif opcion == 3:
                        EliminarAutor()
                    
                    elif opcion == 4:
                        BuscarAutor()

                    elif opcion == 5:
                        break
                    else: 
                        print('Opción incorrecta, ingrese denuevo porfavor.')
                        

                except:
                    print('Seleccione una opción válida, porfavor.')
                


        
        elif opciones == 2:
            Reportes()

        elif opciones == 3:
            break


        else:
         print('Selección no válida, vulva a intentarlo.')
        

    except ValueError:
        print('Ingreso no válido, vuelva a intentar.')
   