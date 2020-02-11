import csv


def guardar_csv(tabla):
    with open('tabla_20200131.csv', 'w', encoding='utf-8') as myfile:
     writer = csv.writer(myfile)
     writer.writerow(['name', 'year', 'geek_rating','average_rating','voters'])
     writer.writerows(tabla)
    return


def guardar_csv(self, tabla):
"""
Esta función recibe los elementos de p.tabla (una lista de 100 tuplas de 5 elements cada una). 
Deberia generar un csv para la primer lista, de no existir el csv. De lo contrario, apendearla al final del csv.
Tambien tengo que generar nombres de variables 
"""
return


class CsvWriterPipeline(object):
    
    def store_game(self,) 
    with open('xx.csv', 'w', encoding='utf-8') as myfile:
     writer = csv.writer(myfile)
     writer.writerow(['name', 'year', 'geek_rating','average_rating','voters'])
     writer.writerows(tabla)
    return