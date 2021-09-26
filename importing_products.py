import numpy as np
import pandas as pd

# Lectura del archivo de productos
x = 0
with open("Data/Productos.txt", "r") as archivo:
    headers_producto = ""
    rows_producto = list()
    for linea in archivo:
        linea = linea.strip()
        if x == 0:
            headers_producto = linea.split()
        else:
            letter_ant = ""
            delimiter = False
            row = ""
            for letter in linea:
                if letter == ' ' and letter_ant == ' ':
                    if delimiter==False :
                        row = row + ";"
                    delimiter = True
                    #row.append(rows)
                else:
                    row = row + letter
                    delimiter = False
                letter_ant = letter
            if len(row.strip().split(';')) == 5 :
                rows = row.strip().split(';')
                rows.pop(4)
                rows_producto.append(rows)
            else :
                rows_producto.append(row.strip().split(';'))

        x = 1 + x

productos_df = pd.DataFrame(rows_producto, columns=headers_producto)

# AGREGAR CLASIFICACION DEL PRODUCTO
clasification_column = list()
for i in productos_df['ProductModel']:
    if str(i).find("Mountain") != -1:
        clasification_column.append('Mountain')
    elif str(i).find("Road") != -1:
        clasification_column.append('Road')
    elif str(i).find("Touring") != -1:
        clasification_column.append('Touring')
    elif str(i).find("Classic") != -1:
        clasification_column.append('Classic')
    else:
        clasification_column.append('No clasificated')

productos_df['Clasification'] = clasification_column
productos_df.to_csv("Data/Productos.csv", sep=";", index= True, index_label="Cons")