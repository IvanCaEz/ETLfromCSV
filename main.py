import csv
import json

"""with open('basket_players.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        print(row)"""

class Jugador:
    def __init__(self, nom, equip, posicio, alçada, pes, edat):
        self.nom = nom
        self.equip = equip
        self.posicio = posicio
        self.alçada = alçada
        self.pes = pes
        self.edat = edat
    
    def __str__(self):
            return f"{self.nom}^{self.equip}^{self.posicio}^{self.alçada}^{self.pes}^{self.edat}"

POUND_TO_KG = 0.45
POLZ_TO_CM = 2.54

def ex_1():
    with open('basket_players.csv') as csvfile:
        dades = csv.reader(csvfile)
        for i, fila in enumerate(dades):
            print(i, ",".join(fila))

def traduct_pos(posicio) -> str:
    match posicio:
        case "Point Guard": posicio = "Base"
        case "Shooting Guard": posicio = "Escolta"
        case "Small Forward": posicio = "Aler"
        case "Power Forward": posicio = "Ala-pivot"
        case "Center": posicio = "Pivot"
    return posicio


def write_to_csv(jugadors: dict, atributs):
    with open('jugadors_basket.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=atributs, delimiter='^')
        writer.writeheader()
        for i, row in enumerate(jugadors["Nom"]):
            # Creem un row amb aquest format per després afegir-ho al writer i que ho escrigui al csv
            row_to_add = {
                atributs[0] : jugadors[atributs[0]][i],
                atributs[1]: jugadors[atributs[1]][i],
                atributs[2]: jugadors[atributs[2]][i],
                atributs[3]: jugadors[atributs[3]][i],
                atributs[4]: jugadors[atributs[4]][i],
                atributs[5]: jugadors[atributs[5]][i]
            }
            writer.writerow(row_to_add)
    


def ex_2() -> dict:
    with open('basket_players.csv') as csvfile:
        dades = csv.reader(csvfile)
        jugadors = {
            "Nom" : [],
            "Equip" : [],
            "Posicio": [],
            "Alçada" : [],
            "Pes": [],
            "Edat": []
        }
        atributs = ['Nom', 'Equip', 'Posicio', 'Alçada', 'Pes', 'Edat']
        
        for i, fila in enumerate(dades):
            # Indexem els jugadors al diccionari
            if i != 0:
                nom = fila[0].split(";")[0]
                equip = fila[0].split(";")[1]
                posicio = traduct_pos(fila[0].split(";")[2])
                alçada = (round(float(fila[0].split(";")[3])*POLZ_TO_CM, 2))
                pes = (round(float(fila[0].split(";")[4])*POUND_TO_KG,2))
                edat = (round(float(fila[0].split(";")[5])))
                jugadors[atributs[0]].append(nom)
                jugadors[atributs[1]].append(equip)
                jugadors[atributs[2]].append(posicio)
                jugadors[atributs[3]].append(alçada)
                jugadors[atributs[4]].append(pes)
                jugadors[atributs[5]].append(edat)

        #Cridem a la funció que crearà i afegirà les dades al nou csv
        write_to_csv(jugadors, atributs)
        return jugadors

def check_jugador_mes_petit(diccionari_jugadors: dict):
    altura_mes_petita = float("inf")
    jugador_mes_petit = ""
    for i in diccionari_jugadors["Alçada"]:
        if float(i) < altura_mes_petita:
            altura_mes_petita = float(i)
            index_jugador_mes_petit = diccionari_jugadors["Alçada"].index(i)
            jugador_mes_petit = diccionari_jugadors["Nom"][index_jugador_mes_petit]
    return f"El jugador més petit és {jugador_mes_petit}, {altura_mes_petita}"

def check_jugador_mes_pesat(diccionari_jugadors: dict):
    pes_mes_gran = 0
    jugador_mes_pesat = ""
    for i in diccionari_jugadors["Pes"]:
        if float(i) > pes_mes_gran:
            pes_mes_gran = float(i)
            index_jugador_mes_pesat= diccionari_jugadors["Pes"].index(i)
            jugador_mes_pesat = diccionari_jugadors["Nom"][index_jugador_mes_pesat]
    return f"El jugador més pesat és {jugador_mes_pesat}, {pes_mes_gran}"

def mitjana_pes_i_alçada(diccionari_jugadors: dict):
    alturas_por_equipo = {}

    for i in range(len(diccionari_jugadors["Nom"])):
        equipo = diccionari_jugadors["Equip"][i]
        altura = float(diccionari_jugadors["Alçada"][i])

        if equipo not in alturas_por_equipo:
            alturas_por_equipo[equipo] = []

            alturas_por_equipo[equipo].append(altura)

    # Calculamos la altura media para cada equipo
    for equipo, alturas in alturas_por_equipo.items():
                altura_media = sum(alturas) / len(alturas)
                print(f"Altura media del equipo {equipo}: {altura_media:.2f} centímetros")



    pesos_por_equipo = {}

    for i in range(len(diccionari_jugadors["Nom"])):
        equipo = diccionari_jugadors["Equip"][i]
        peso = float(diccionari_jugadors["Pes"][i])

        if equipo not in pesos_por_equipo:
            pesos_por_equipo[equipo] = []

        pesos_por_equipo[equipo].append(peso)

    # Calculamos el peso medio para cada equipo
    for equipo, pesos in pesos_por_equipo.items():
        peso_medio = sum(pesos) / len(pesos)
        print(f"Peso medio del equipo {equipo}: {peso_medio:.2f} kilogramos")

def check_jugadors_posicions(diccionari_jugadors: dict):
    jugadores_por_posicion = {}

    for posicion in diccionari_jugadors["Posicio"]:
        if posicion not in jugadores_por_posicion:
            jugadores_por_posicion[posicion] = 0
        jugadores_por_posicion[posicion] += 1

    # Imprimimos el total de jugadores por posición
    for posicion, cantidad in jugadores_por_posicion.items():
        print(f"Total de jugadores en la posición {posicion}: {cantidad}")

def check_edats_jugadors(diccionari_jugadors: dict):
    jugadores_por_edades = {}

    for edad in diccionari_jugadors["Edat"]:
        grupo_edad = edad // 10 * 10  # Redondeamos la edad al múltiplo de 10 más cercano
        if grupo_edad not in jugadores_por_edades:
            jugadores_por_edades[grupo_edad] = 0
        jugadores_por_edades[grupo_edad] += 1

    # Imprimimos la distribución de jugadores por grupo de edades
    for grupo_edad, cantidad in sorted(jugadores_por_edades.items()):
        print(f"Jugadores en el grupo de edad {grupo_edad}-{grupo_edad+9}: {cantidad}")

def ex_4():
    json_file_path = 'json_basket_players.json'
    data = []
    with open('basket_players.csv') as csvfile:
        dades = csv.DictReader(csvfile, delimiter=";")
        for i, row in enumerate(dades):
            jugador = {
            "Nom": row["Name"],
            "Equip": row["Team"],
            "Posicio": row["Position"],
            "Alçada": float(row["Heigth"]),
            "Pes": float(row["Weigth"]),
            "Edat": float(row["Age"])
            }
            data.append(jugador)
    with open(json_file_path, 'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)

def ex3():
   diccionari_jugadors = ex_2()
   continuar = True
   print("Selecciona les estadístiques que vols veure:")
   print("1-Nom del jugador amb el pes més alt.\n2-Nom del jugador amb l’alçada més petita.\n3-Mitjana de pes i alçada de jugador per equip.\n4-Recompte de jugadors per posició.\n5-Distribució de jugadors per edat.")
   print("6-Sortir")
   while continuar:
       seleccio = int(input("Selecciona una opció: "))
       match seleccio:
           case 1: print(check_jugador_mes_petit(diccionari_jugadors))
           case 2: print(check_jugador_mes_pesat(diccionari_jugadors))
           case 3: print(mitjana_pes_i_alçada(diccionari_jugadors))
           case 4: print(check_jugadors_posicions(diccionari_jugadors))
           case 5: print(check_edats_jugadors(diccionari_jugadors))
           case 6: 
               print("Adéu")
               continuar = False
        
ex_4()

