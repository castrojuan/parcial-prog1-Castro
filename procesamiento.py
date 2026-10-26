from validaciones import validar_nombre, valida_nota, valida_entero, validar_cantidad_alumnos




def crear_lista(cantidad: int, valor_inicial: int | float | str) -> list:
    """La funcion recibe un parametro por posicion y crea una lista inicial, 
       para definir la cantidad de elementos que tendra

       Parametro: int | float | string para cada lista a crear 
       Return: lista para cada tipo de datos
    """
    lista = [valor_inicial] * cantidad
    
    return lista




def cargar_alumnos(cantidad: int, nombre: list, nota1: list, nota2: list, promedio: list):
    """La funcion pide el ingreso de nombre, nota1, nota2.
        sobrescribe las listas de cada variable y al mismo tiempo que valida que 
        los datos ingresados esten dentro del rango permitido  

        Argumento: list[int | str | float] para cargar las respectivas listas
        Return: listas[int | str | float] cargadas previa validacion de datos ingresados
    """ 

    for i in range(cantidad):

        nombre_ingresado = input(f"Ingrese nombre del alumno {i + 1}: ")
        while not validar_nombre(nombre_ingresado): 
            nombre_ingresado = input(f"Ingrese nombre del alumno {i + 1}: ")
        nombre[i] = nombre_ingresado    

            
        nota1_ingresada = valida_entero(f"Ingrese la nota del 1er parcial: ") 
        while not valida_nota(nota1_ingresada):
            print("Invalido. Ingrese una nota entre 0 y 10.")
            nota1_ingresada = valida_entero(f"Ingrese la nota del 1er parcial: ")
        nota1[i] = nota1_ingresada


        nota2_ingresada = valida_entero(f"Ingrese la nota del 2do parcial: ") 
        while not valida_nota(nota2_ingresada):
            print("Invalido, ingrese una nota entre 0 y 10.")
            nota2_ingresada = valida_entero(f"Ingrese la nota del 2do parcial: ")
        nota2[i] = nota2_ingresada


        promedio[i] = calcular_promedio(nota1[i], nota2[i])

    return nombre, nota1, nota2, promedio    




def inicializar_listas_paralelas()-> list[float | int | str]:
    """ La funcion valida la cantidad solicitada, validando que este en el rango permitido 
        Invoca a la funcion de crear_lista y luego a la de cargar_alumnos

        Argumento: list[int | str | float] para crear y cargar las respectivas listas
        Return: listas[int | str | float] cargadas previa validacion de datos ingresados
    """ 
    cantidad = validar_cantidad_alumnos()
    nombre = crear_lista(cantidad, "")
    nota1 = crear_lista(cantidad, 0)
    nota2 = crear_lista(cantidad, 0)
    promedio = crear_lista(cantidad, 0.0)

    cargar_alumnos(cantidad, nombre, nota1, nota2, promedio)
    
    return cantidad, nombre, nota1, nota2, promedio  




def calcular_promedio(nota1: list[float], nota2: list[float])-> list[float]:
    """La funcion calcula el promedio de dos datos float guardados en listas paralelas

        Argumento: list [float] para realizar la operacion aritmetica

        Return: list[float] El resultado de la operacion guardado en lista promedio
    """ 
    resultado = (float(nota1) + float(nota2)) / 2
    return resultado          




def mostrar_listado(cantidad: int, nombre: list[str], nota1: list[int], nota2: list[int], promedio: list[float]) -> str:
    """La funcion muestra las listas paralelas en el orden que fueron ingresadas
    
    Argumento: int, list [float | int | str] 
    
    Return: list[str] devuelve una cadena de caracteres
    """ 
    resultado = ""

    for i in range(cantidad):
        resultado += f"\nAlumno: {nombre[i]} == Nota 1er parcial: {nota1[i]} == Nota 2do parcial:  {nota2[i]} == Promedio: {promedio[i]}\n"
        
    return resultado
    



def inicio_menu():
    """La funcion solo imprime un menu inicial al inicio del archivo main, 
        para mostrar las opciones al usuario
    """
    print("=" * 5, "NOTAFACIL", "=" * 5, "\n1. Cargar Alumno\n2. Mostrar listado\n3. Mostrar estadisticas"
        "\n4. Ver ranking (ordenado)\n5. Buscar alumno\n6. Juegos con un nombre\n0. Salir\n")
    


      
def promedio_general(cantidad: int,promedio: list[float | int]) ->float:
    """La funcion acumula todos los valores de la lista promedio y luego realiza el 
       calculo del promedio general de todos los alumnos

       Argumento: int para recorrer indice list[float] recorre la lista y sumar los valores
       Return: devuelve un valor float con el promedio general del curso
    """
    acumulador_promedio = 0.0
    for i in range(cantidad):
        acumulador_promedio += promedio[i] 
    
    resultado = acumulador_promedio / cantidad 

    return resultado 


 

def promedios_min_max(cantidad: int, promedio:list[float], nombre: list[str])->str:
    """La funcion declara 2 variables maximas y 2 minimas, y recorre la lista de promedios
        con bucle for para comparar los valores. Guarda el valor mas alto y el mas bajo, 
        paralelamente con el nombre del alumno en esa posicion

        Argumento:   int, list[float | str] indice a recorrer y nombre y promedio del alumno en su posicion
        Return: devuelve cadena de caracteres con el promedio mas alto y mas bajo, con sus respectivos nombre
    """
    minimo = promedio [0]
    maximo = promedio [0]
    nombre_max = nombre[0]
    nombre_min = nombre[0]
    
    for i in range(1, cantidad):
        if promedio[i] < minimo:
            minimo = promedio[i]
            nombre_min = nombre[i]
        
        elif promedio[i] > maximo:
            maximo = promedio[i]
            nombre_max = nombre[i] 
        
    
    resultado = f"\nMejor promedio {nombre_max}: {maximo}\nPeor promedio {nombre_min}: {minimo}"
            

    return resultado
        
            


def ordena_alumnos_por_condicion(promedio: list[float], cantidad: int)->str:
    """ La funcion recorre la lista de promedios, y utiliza 3 contadores para filtrar los promedios
        segun su condicion. Contador Promociona aumenta si el promedio es >=6   Contador Aprueba aumenta 
        si el promedio es entre 4 y 5   y contador desaprueba aumenta si es entre 0 y 3

        Argumentos: int  para recorrer indice y list[float] para comparar los valores
        Return: devuelve cadena de caracteres con el resultado del filtro  
    """
    promociona = 0
    aprueba = 0 
    desaprueba = 0    
    for i in range(cantidad):
        if promedio[i] >= 6:
            promociona += 1
            
        if promedio[i] < 4:
            desaprueba += 1
            
        if promedio[i] >= 4 and promedio[i] < 6:
            aprueba += 1
            
    resultado = f"\nAlumnos que promocionan:{promociona}\nAlumnos que aprueban: {aprueba}\nAlumnos que desaprueban: {desaprueba}"

    return resultado


    


def buscar_alumno(cantidad: int, nombre: list[str], nota1: list[int], nota2: list[int], promedio:list)->str:
    """La funcion pide al usuario ingresar un nombre y recorre el indice. Si encuentra el nombre, 
       muestra los datos cargados en las listas paralelas. Si no lo encuentra, le avisa que no lo encontro y
       sale de la opcion, por si el usuario quiere elegir otra opcion.
       Si desea volver a buscar, tiene que elegir otra vez la opcion buscar_alumno

       Argumentos:cantidad: int  como indice para iterar 
                  nombre: list[str] dato clave de la funcion que traera el resultado
                  nota1: list[int] datos a mostar una vez encontrado
                  nota2: list[int]
                  promedio:list[float]
        Return: cadena de caracteres con los datos guardados en las listas          
    """
    valido = False

    while not valido:

        objetivo = input("Ingrese el nombre del alumno: ")
    
        for i in range(cantidad):
            if nombre[i] == objetivo:
                reporte = f"\nAlumno {nombre[i]}\nNota 1er parcial: {nota1[i]}\nNota 2do parcial: {nota2[i]}\nPromedio: {promedio[i]}"
                valido = True 
                break
        
            if not valido:
                reporte = f"\nalumno {objetivo} no se encuentra en la lista"
                valido = True # Aca deja de iterar porque quiero que salga. Si el usuario quiere seguir buscando, vuelve a apretar 5
        
    return reporte            

    
        
            
def ingresar_alumno(nombre: list[str])->str:
    """ La funcion pide al usuario ingresar un nombre. Si lo encuentra devuelve el nombre, 
        y si no le dice que no lo encontro.
        Argumento: list[str] para buscar el dato en la lista de nombres
        Return: devuelve cadena str
    """  
    encontrado = False
    objetivo = input(" ingresar nombre ")
    for i in range(len(nombre)):
        if nombre[i] == objetivo:
            encontrado = True
            return objetivo

    if not encontrado:
        print("\nEl alumno no se encuentra en la lista.")



def contador_vocales(nombre: list[str])->int:
    """La funcion recibe el argumento por posicion de la funcion ingresar_alumno
        e itera sobre el dato, utilizando un contador cada vez que encuentra una vocal.

        Argumento: list[str] para asegurar que el nombre ingresado este dentro de la lista
        Return: devuelve un entero, indicando la cantidad de vocales que tiene el nombre
    """    
    vocales = "aeiou"
    contador = 0
    for i in range(len(nombre)):

        for j in range(len(vocales)):
            if nombre[i] == vocales[j]:
                contador += 1

    print(f"\nCantidad de vocales en {nombre} : {contador}")            
    return contador
          

        
def invertir_nombre(nombre:list[str])->list[str]:
    """La funcion recibe un parametro desde la funcion ingresar_nombre,y utiliza busqueda lineal 
       para retornar la cadena ingresada de forma invertida

       Argumento: list[str] cadena de caracteres dentor de una lista
       Return : la cadena de caracteres, de forma invertida
    """   
    return nombre[::-1]



def ordena_ascendente(nombre: list[str], promedio: list[float])->str:
    """La funcion muestra un ranking de mejor a peor promedio,junto con el nombre 
       utilizando metodo de ordenamiento burbuja.

        Argumento: list[str] lista de alumnos, para cambiar segun ordenamiento
                   list[float] lista de promedios a ordenar

        Return : cadena de caracteres con el ranking de mejor a peor promedio
    """ 

    ranking = ""  
    n = len(nombre)
    
    for i in range(n):
        
        for j in range(n - 1):
            
            if promedio[j] < promedio[j + 1]:
                auxiliar = promedio[j + 1]
                aux_nombre = nombre[j+ 1]
                promedio[ j + 1] = promedio[j]
                nombre[j+1] = nombre[j]
                promedio[j] = auxiliar
                nombre[j] = aux_nombre          

    for i in range(n):
        ranking += f"\nPuesto {i + 1} Alumno: {nombre[i]} con un Promedio de : {promedio[i]}"
        

    return ranking          



#Extra 
#case 7:
    if verificar_carga_inicial(cantidad):
        busqueda = modificar_alumno(cantidad, nombre, nota1, nota2, promedio) 
        print(busqueda)
#
#
#def modificar_alumno(cantidad: int, nombre: list[str], nota1: list[int], nota2: list[int], promedio:list)->str:

    valido = False

    while not valido:

        objetivo = input("Ingrese el nombre del alumno: ")
    
        for i in range(cantidad):
            if nombre[i] == objetivo:
                reporte = f"\nAlumno {nombre[i]}\nNota 1er parcial: {nota1[i]}\nNota 2do parcial: {nota2[i]}\nPromedio: {promedio[i]}"
                valido = True
                modificar_datos = input(f"modificar nombre del alumno {i + 1}: ")
                while not validar_nombre(modificar_datos): 
                    modificar_datos = input(f"Ingrese nombre del alumno {i + 1}: ")
                nombre[i] = modificar_datos

                nota1_modificar = valida_entero(f"corrija la nota del 1er parcial: ") 
                while not valida_nota(nota1_modificar):
                    print("Invalido. Ingrese una nota entre 0 y 10.")
                    nota1_modificar = valida_entero(f"Ingrese la nota del 1er parcial: ")
                nota1[i] = nota1_modificar
                
                
                nota2_corregir = valida_entero(f"Corrija la nota del 2do parcial: ") 
                while not valida_nota(nota2_corregir):
                    print("Invalido, ingrese una nota entre 0 y 10.")
                    nota2_corregir = valida_entero(f"Ingrese la nota del 2do parcial: ")
                nota2[i] = nota2_corregir
                
                promedio[i] = calcular_promedio(nota1[i], nota2[i]) 

                reporte = f"\nAlumno {nombre[i]}\nNota 1er parcial: {nota1[i]}\nNota 2do parcial: {nota2[i]}\nPromedio: {promedio[i]}"
                break
        
            if not valido:
                reporte = f"\nalumno {objetivo} no se encuentra en la lista"
                valido = True # Aca deja de iterar porque quiero que salga. Si el usuario quiere seguir buscando, vuelve a apretar 5
        
    return reporte 





      


