from validaciones import *
from procesamiento import *

inicio_menu()

nombre = [""]
nota1 = [0]
nota2 = [0]
promedio = [0.0]
cantidad = 0
salir_menu = False



while not salir_menu:

    opcion = valida_entero("==Elija una opcion: 1-Cargar alumno| 2-Mostar listado| 3-Estadisticas| 4-Ranking| 5-Busqueda| 6-Juego| 0-Salir ")
    
    match opcion:
        
        case 1:
            
            cantidad, nombre, nota1, nota2, promedio = inicializar_listas_paralelas()
            
        case 2:
            if verificar_carga_inicial(cantidad):
                despliega_listado = mostrar_listado(cantidad,nombre, nota1, nota2, promedio)
                print(despliega_listado)
                          
        case 3:
            if verificar_carga_inicial(cantidad):
                promedios = promedio_general(cantidad, promedio)
                print(f"===el promedio general del curso es {promedios}====")

                estadistica = promedios_min_max(cantidad, promedio, nombre)
                print(estadistica)

                condicion = ordena_alumnos_por_condicion(promedio, cantidad)
                print(condicion)
                
        case 4:
            if verificar_carga_inicial(cantidad):
                ranking = ordena_ascendente(nombre, promedio) 
                print(ranking)
               
        case 5:
            if verificar_carga_inicial(cantidad):
                busqueda = buscar_alumno(cantidad, nombre, nota1, nota2, promedio) 
                print(busqueda) 
          
        case 6:
            if verificar_carga_inicial(cantidad):
                nombre_ingresado_valido = ingresar_alumno(nombre)
                if not nombre_ingresado_valido:
                    continue
                contador_vocales(nombre_ingresado_valido)
                print(invertir_nombre(nombre_ingresado_valido))

        case 0:
            print("Saliendo del programa\nGracias")
            salir_menu = True
            datos_cargados = True

        case _:
            print("Opcion no valida. Ingrese una opcion del menu ")
                         
