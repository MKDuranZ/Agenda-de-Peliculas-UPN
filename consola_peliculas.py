import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10): hora_formato = "0"+ str(hora//100)
    else: hora_formato = str(hora//100)
    
    if (hora%100 < 10): min_formato = "0"+ str(hora%100)
    else: min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

# --- LAS FUNCIONES ORIGINALES ---
def ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) -> None:
    peli_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    print("La pelicula mas larga es:")
    mostrar_informacion_pelicula(peli_larga)

def ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) -> None:
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    print("La duracion promedio de tu agenda es:", promedio)

def ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, anio: int) -> None:
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, anio)
    print("Las peliculas estrenadas despues del", anio, "son:", estrenos)

def ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) -> None:
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    print("Tienes", cantidad, "peliculas con clasificacion 18+ en tu agenda.")

def ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) -> None:
    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    if pelicula is None: print("No hay ninguna pelicula con este nombre")
    else:
        nuevo_dia = input("Ingrese el nuevo dia (ej: Lunes): ")
        nueva_hora = int(input("Ingrese la nueva hora (formato 24h, ej: 1430): "))
        control = input("Desea aplicar el control de horario? (Si/No): ")
        control_horario = True if control.lower() == "si" else False
        se_pudo = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
        if se_pudo: print("Pelicula reagendada con exito.")
        else: print("Error: Conflicto de horario o reglas.")

def ejecutar_decidir_invitar(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) -> None:
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    if pelicula is None: print("No hay ninguna pelicula con este nombre")
    else:
        edad = int(input("Ingrese la edad del invitado: "))
        auth_padres = input("¿Tiene autorizacion de los padres? (Si/No): ")
        autorizado = True if auth_padres.lower() == "si" else False
        puede_ver = mod.decidir_invitar(pelicula, edad, autorizado)
        if puede_ver: print("El invitado SI puede ver la pelicula.")
        else: print("El invitado NO puede ver la pelicula.")

# --- NUEVAS FUNCIONES AGREGADAS ---
def ejecutar_buscar_pelicula(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) -> None:
    print("--- BUSCAR PELICULA ---")
    nombre = input("Ingrese el nombre exacto de la pelicula: ")
    peli = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    if peli is not None:
        print("\n¡Pelicula encontrada!")
        mostrar_informacion_pelicula(peli)
    else:
        print("\nNo se encontró ninguna pelicula con ese nombre.")

def ejecutar_crear_pelicula(peliculas_adicionales: list) -> None:
    print("--- CREAR NUEVA PELICULA ---")
    nom = input("Nombre: ")
    gen = input("Genero(s) (ej: Accion, Drama): ")
    dur = int(input("Duracion (minutos): "))
    anio = int(input("Año de estreno: "))
    clas = input("Clasificacion (Todos, 7+, 13+, 16+, 18+): ")
    dia = input("Dia de la semana (ej: Lunes): ")
    hora = int(input("Hora (formato 24h, ej: 1430): "))
    
    nueva_peli = mod.crear_pelicula(nom, gen, dur, anio, clas, hora, dia)
    peliculas_adicionales.append(nueva_peli)
    print("\n¡Pelicula guardada exitosamente para la visualizacion de la agenda!")

# --- LÓGICA PRINCIPAL DE LA APLICACIÓN ---
def iniciar_aplicacion():
    p1 = mod.crear_pelicula("Shrek", "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    p2 = mod.crear_pelicula("Get Out", "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    p3 = mod.crear_pelicula("Icarus", "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    p4 = mod.crear_pelicula("Inception", "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    p5 = mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    p6 = mod.crear_pelicula("Toy Story", "Familiar, Animación", 81, 1995, 'Todos', 1000, "Sábado")
    p7 = mod.crear_pelicula("Matrix", "Acción, Ciencia-Ficción", 136, 1999, '13+', 2000, "Viernes")
    p8 = mod.crear_pelicula("El Padrino", "Drama, Crimen", 175, 1972, '18+', 2100, "Sábado")
    p9 = mod.crear_pelicula("Coco", "Familiar, Animación", 105, 2017, 'Todos', 1500, "Domingo")
    p10 = mod.crear_pelicula("Joker", "Drama, Suspenso", 122, 2019, '18+', 2200, "Martes")
    p11 = mod.crear_pelicula("Interstellar", "Ciencia-Ficción, Drama", 169, 2014, '13+', 1800, "Jueves")
    p12 = mod.crear_pelicula("Nuestro Planeta", "Documental, Naturaleza", 50, 2019, 'Todos', 900, "Lunes")
    p13 = mod.crear_pelicula("El Conjuro", "Terror", 112, 2013, '18+', 2300, "Viernes")
    p14 = mod.crear_pelicula("Up", "Familiar, Aventura", 96, 2009, 'Todos', 1600, "Miércoles")
    p15 = mod.crear_pelicula("Gladiador", "Acción, Drama", 155, 2000, '16+', 1930, "Domingo")
    p16 = mod.crear_pelicula("Parasite", "Suspenso, Drama", 132, 2019, '16+', 2030, "Jueves")
    p17 = mod.crear_pelicula("Buscando a Nemo", "Familiar, Animación", 100, 2003, 'Todos', 1100, "Sábado")
    p18 = mod.crear_pelicula("Mad Max", "Acción, Ciencia-Ficción", 120, 2015, '16+', 1700, "Lunes")
    p19 = mod.crear_pelicula("El Resplandor", "Terror, Suspenso", 146, 1980, '18+', 2230, "Sábado")
    p20 = mod.crear_pelicula("Avatar", "Ciencia-Ficción, Acción", 162, 2009, '13+', 1400, "Domingo")
    
    # Lista extra para guardar las nuevas peliculas que se vayan creando en consola
    peliculas_adicionales = []

    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas" +"\n"+("-"*50))
        # Imprimimos las 20 originales + las que se hayan creado
        bd_impresion = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20] + peliculas_adicionales
        for i in range(len(bd_impresion)):
            print("Pelicula " + str(i + 1))
            mostrar_informacion_pelicula(bd_impresion[i])
            print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, peliculas_adicionales)

        if ejecutando:
            input("Presione ENTER para continuar ... ")

def mostrar_menu_aplicacion(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, peliculas_adicionales) -> bool:
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Buscar pelicula por nombre")
    print(" 8 - Crear nueva pelicula")
    print(" 9 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    elif opcion_elegida == "3":
        anio_input = int(input("Ingrese el año a partir del cual buscar estrenos: "))
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, anio_input)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20) 
    elif opcion_elegida == "7":
        ejecutar_buscar_pelicula(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
    elif opcion_elegida == "8":
        ejecutar_crear_pelicula(peliculas_adicionales)
    elif opcion_elegida == "9":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es valida.")
    
    return continuar_ejecutando

iniciar_aplicacion()