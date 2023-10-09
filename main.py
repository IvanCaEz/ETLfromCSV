import csv

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
    pes = 0.0
    alçada = 0.0
    for i in diccionari_jugadors["Alçada"]:
        alçada += float(i)
    
    for i in diccionari_jugadors["Pes"]:
        pes += float(i)
    print(pes, alçada)


def ex3():
   diccionari_jugadors = ex_2()

   print(check_jugador_mes_petit(diccionari_jugadors))
   print(check_jugador_mes_pesat(diccionari_jugadors))
   print(mitjana_pes_i_alçada(diccionari_jugadors))

ex3()

