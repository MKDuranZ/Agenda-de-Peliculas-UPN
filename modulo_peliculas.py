"""
Agenda de peliculas.
Módulo de cálculos.
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    d = {}
    d['nombre'] = nombre
    d['genero'] = genero
    d['duracion'] = duracion
    d['anio'] = anio
    d['clasificacion'] = clasificacion
    d['hora'] = hora
    d['dia'] = dia
    return d

# --- LÓGICA DE LA IMAGEN APLICADA A 20 PELÍCULAS ---
def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, p11: dict, p12: dict, p13: dict, p14: dict, p15: dict, p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict:
    bd = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    for i in range(len(bd)):
        if bd[i]['nombre'] == nombre_pelicula:
            return bd[i]
    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, p11: dict, p12: dict, p13: dict, p14: dict, p15: dict, p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> dict:
    bd = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    lt = []
    for i in range(len(bd)):
        lt.append(bd[i]['duracion'])
    return bd[lt.index(max(lt))]

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, p11: dict, p12: dict, p13: dict, p14: dict, p15: dict, p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> str:
    bd = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    l_promedio = []
    for i in range(len(bd)):
        l_promedio.append(bd[i]['duracion'])
    
    promedio = sum(l_promedio) / len(l_promedio)
    h = int(promedio // 60)
    m = int(promedio % 60)
    
    if h < 10: str_h = "0" + str(h)
    else: str_h = str(h)
        
    if m < 10: str_m = "0" + str(m)
    else: str_m = str(m)
        
    return str_h + ":" + str_m

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, p11: dict, p12: dict, p13: dict, p14: dict, p15: dict, p16: dict, p17: dict, p18: dict, p19: dict, p20: dict, anio: int) -> str:
    bd = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    l_estrenos = []
    for i in range(len(bd)):
        if bd[i]['anio'] > anio:
            l_estrenos.append(bd[i]['nombre'])
            
    if len(l_estrenos) == 0: return "Ninguna"
    else: return ", ".join(l_estrenos)

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, p11: dict, p12: dict, p13: dict, p14: dict, p15: dict, p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> int:
    bd = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    count = 0
    for i in range(len(bd)):
        if bd[i]['clasificacion'] == '18+':
            count += 1
    return count

def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str, control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, p6: dict, p7: dict, p8: dict, p9: dict, p10: dict, p11: dict, p12: dict, p13: dict, p14: dict, p15: dict, p16: dict, p17: dict, p18: dict, p19: dict, p20: dict) -> bool:
    bd = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    
    if control_horario:
        if 'Documental' in peli['genero'] and nueva_hora >= 2200: return False
        if 'Drama' in peli['genero'] and nuevo_dia == 'Viernes': return False
        if nuevo_dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']:
            if nueva_hora >= 2300 or nueva_hora < 600: return False

    min_inicio_nueva = (nueva_hora // 100) * 60 + (nueva_hora % 100)
    min_fin_nueva = min_inicio_nueva + peli['duracion']

    for i in range(len(bd)):
        if bd[i]['nombre'] != peli['nombre']:
            if bd[i]['dia'] == nuevo_dia:
                hora_eval = bd[i]['hora']
                min_inicio_eval = (hora_eval // 100) * 60 + (hora_eval % 100)
                min_fin_eval = min_inicio_eval + bd[i]['duracion']
                if min_inicio_nueva < min_fin_eval and min_inicio_eval < min_fin_nueva:
                    return False

    peli['hora'] = nueva_hora
    peli['dia'] = nuevo_dia
    return True

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    if edad_invitado >= 18: return True
    if edad_invitado < 15 and 'Terror' in peli['genero']: return False
    if edad_invitado <= 10 and 'Familiar' not in peli['genero']: return False

    clasif = peli['clasificacion']
    edad_requerida = 0
    if clasif == '7+': edad_requerida = 7
    elif clasif == '13+': edad_requerida = 13
    elif clasif == '16+': edad_requerida = 16
    elif clasif == '18+': edad_requerida = 18

    if edad_invitado < edad_requerida:
        if 'Documental' in peli['genero']: return True 
        else: return autorizacion_padres

    return True