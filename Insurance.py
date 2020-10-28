import csv
archivo = open("insurance.csv")

for linea in csv.DictReader(archivo):
    print(linea["age"])
    