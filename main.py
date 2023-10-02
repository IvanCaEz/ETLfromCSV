import csv

"""with open('basket_players.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        print(row)"""


def ex_1():
    with open('basket_players.csv') as csvfile:
        dades = csv.reader(csvfile)
        for i, fila in enumerate(dades):
            print(i, ",".join(fila))
        

def ex_2():
    with open('basket_players.csv') as csvfile:
        dades = csv.reader(csvfile)
        atributs = ['Nom', 'Equip', 'Posicio', 'Alçada', 'Pes', 'Edat']
        for i, fila in enumerate(dades):
            atributs['Nom'] = fila[0].split(";")[0]
            atributs['Equip'] = fila.partition(";")[1]
            atributs['Posicio'] = fila.partition(";")[2]
            atributs['Alçada'] = fila.partition(";")[3]
            atributs['Pes'] = fila.partition(";")[4]
            atributs['Edat'] = fila.partition(";")[5]
        
ex_2()
