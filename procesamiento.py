from validaciones import validar_nombre, valida_nota, valida_entero, validar_cantidad_alumnos

def crear_lista(cantidad: int, valor_inicial: int | float | str) -> list:
    """
    """
    lista = [valor_inicial] * cantidad
    
    return lista

def cargar_alumnos(cantidad: int, nombre: list, nota1: list, nota2: list, promedio: list):
    """La funcion pide el ingreso de nombre, nota1, nota2.
    Carga las listas de cada variable y al mismo tiempo que valida que 
    los datos ingresados esten dentro del rango permitido  
    """ 

    for i in range(cantidad):

        nombre_ingresado = input(f"Ingrese nombre del alumno {i + 1}: ")
        while not validar_nombre(nombre_ingresado): 
            nombre_ingresado = input(f"Ingrese nombre del alumno {i+1}: ")
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
    """
    """
    cantidad = validar_cantidad_alumnos()
    nombre = crear_lista(cantidad, "")
    nota1 = crear_lista(cantidad, 0)
    nota2 = crear_lista(cantidad, 0)
    promedio = crear_lista(cantidad, 0.0)

    cargar_alumnos(cantidad, nombre, nota1, nota2, promedio)
    
    return cantidad, nombre, nota1, nota2, promedio  







def calcular_promedio(nota1: list[float], nota2: list[float])-> bool:
    resultado = (float(nota1) + float(nota2)) / 2
    return resultado          




def mostrar_listado(cantidad: int, nombre: list[str], nota1: list[int], nota2: list[int], promedio: list[float]) -> str:
    resultado = ""

    for i in range(cantidad):
        resultado += f"\nAlumno: {nombre[i]} == Nota 1er parcial: {nota1[i]} == Nota 2do parcial:  {nota2[i]} == Promedio: {promedio[i]}\n"
        
    return resultado
    
    

def inicio_menu():
    
    print("=" * 5, "NOTAFACIL", "=" * 5, "\n1. Cargar Alumno\n2. Mostrar listado\n3. Mostrar estadisticas"
        "\n4. Ver ranking (ordenado)\n5. Buscar alumno\n6. Juegos con un nombre\n0. Salir\n")
    
        
      
def promedio_general(cantidad: int,promedio: list[float | int]) ->float:
    acumulador_promedio = 0.0
    for i in range(cantidad):
        acumulador_promedio += promedio[i] 
    
    resultado = acumulador_promedio / cantidad 

    return resultado 

 

def promedios_min_max(cantidad, promedio, nombre)->str:
    
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
        
            


def ordena_alumnos_por_condicion(promedio, cantidad):
    
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


    


def buscar_alumno(cantidad,nombre, nota1, nota2, promedio)->str:

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

    
        

            
def ingresar_alumno(nombre):
    encontrado = False
    objetivo = input(" ingresar nombre ")
    for i in range(len(nombre)):
        if nombre[i] == objetivo:
            encontrado = True
            return objetivo

    if not encontrado:
        print("\nEl alumno no se encuentra en la lista.")


def contador_vocales(nombre):
    vocales = "aeiou"
    contador = 0
    for i in range(len(nombre)):

        for j in range(len(vocales)):
            if nombre[i] == vocales[j]:
                contador += 1

    print(f"\nCantidad de vocales en {nombre} : {contador}")            
    return contador
          
        
def invertir_nombre(nombre):
    return nombre[::-1]

def ordena_ascendente(nombre, promedio)->str:

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










      


