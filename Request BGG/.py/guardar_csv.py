import csv


def guardar_csv(tabla):
    with open('tabla_20200131.csv', 'w', encoding='utf-8') as myfile:
     writer = csv.writer(myfile)
     writer.writerow(['name', 'year', 'geek_rating','average_rating','voters'])
     writer.writerows(tabla)
    return