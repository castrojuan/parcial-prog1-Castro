

def valida_entero(entrada: str) -> int:
    """
    La funcion pide una entrada al usuario
    verifica que no este vacia, y  que sea un caracter numerico valido.

    Parametro:
    mensaje en (str) para solicitar una entrada 
       
    Return: 
    int: argumento validado y convertido a entero
    """

    valido = False
    cantidad = ""

    while not valido:
        cantidad = input(entrada)
        if len(cantidad) == 0:
            print("Debe contener al menos un numero. ")
            continue

        valido = True

        for i in range(len(cantidad)):
            caracter = cantidad[i]
            if not ("0" <= caracter <= "9"):
                valido = False
                print(f"{cantidad} no es un caracter valido. ")
                break

    return int(cantidad)    


def validar_cantidad_alumnos() ->int:
    """La funcion pide un numero y validando que sea numero entero a 
       traves de la funcion valida_entero, y verifica que este dentro del rango
        permitido 1-30
       
        Return: 
        int: numero dentro del rango permitido
    """

    valido = False
    cantidad = 0

    while not valido:
        cantidad = valida_entero("Ingrese la cantidad de alumnos que quiere registrar ")

        if 1 <= cantidad <= 30:
            valido = True

        else:
            print("La cantidad ingresada es invalida. Debe ser entre 1-30 ")

    return cantidad        




def validar_nombre(nombre:list[str]) -> bool:
    """
        La funcion recibe un argumento y verifica que sea un nombre de al menos 5 caracteres, 
        que contenga solo letras minusculas, mayusculas, o espacios

        Argumento: list[str] para validar el nombre       
        Return: booleano True si el nombre es valido
    """
    
    if len(nombre) < 5:
        print("El nombre debe contener al menos 5 caracteres ")
        return False 

    for i in range(len(nombre)):
        caracter = nombre[i]  
        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z" 
        espacio = caracter == " "

        if not (minuscula or mayuscula or espacio):
            return False 

    return True


            
def valida_nota(nota: list[int])-> bool:
    """
        La funcion recibe un numero y valida que sea una nota valida entre el 0 y el 10

        Argumento:list[int] nota a evaluar

        Return: bool true si es valido
    """    
    valido = False

    if nota >= 0 and nota <= 10:
        valido = True
        
    return valido  


def verificar_carga_inicial(cantidad: int) -> bool:
    """
    Verifica si la cantidad de alumnos/listas registrada es mayor a cero.
    Si es cero, le vuelve a pedir que ingrese una opcion.

    Argumento: int para verificar el valor de cantidad
    Return: bool False si cantidad = 0 y le pide que registre la lista primero
    """
    if cantidad == 0:
        print("\nPrimero debe registrar los alumnos. Ingrese 1 para el registro, o presione 0 para salir del menu ")
        return False
        
    return True
        
        









        



