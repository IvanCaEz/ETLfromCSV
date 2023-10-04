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


def ex_2():
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
                alçada = str(round(float(fila[0].split(";")[3])*POLZ_TO_CM, 2))
                pes = str(round(float(fila[0].split(";")[4])*POUND_TO_KG,2))
                edat = str(round(float(fila[0].split(";")[5])))
                jugadors[atributs[0]].append(nom)
                jugadors[atributs[1]].append(equip)
                jugadors[atributs[2]].append(posicio)
                jugadors[atributs[3]].append(alçada)
                jugadors[atributs[4]].append(pes)
                jugadors[atributs[5]].append(edat)

        #Cridem a la funció que crearà i afegirà les dades al nou csv
        write_to_csv(jugadors, atributs)

ex_2()

