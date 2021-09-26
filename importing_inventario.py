import numpy as np
import pandas as pd
x = 0
with open("Data/Inventario.txt", "r") as archivo:
    headers_inventario = ""
    rows_inventario = list()
    for linea in archivo:
        linea = linea.strip()
        if x == 0:
            headers_inventario = linea.split()
        else:
            letter_ant = ""
            delimiter = False
            row = ""
            for letter in linea:
                if letter == ' ' and letter_ant == ' ':
                   if delimiter==False :
                        row = row + ";"
                        delimiter = True
                else:
                    #row.append(rows)
                    row = row + letter
                    delimiter = False
                letter_ant = letter
            row = row.replace('00:00:00.000', '00:00:00.000;')
            rows_inventario.append(row.strip().split(';'))
        x = 1 + x
    inventario_df = pd.DataFrame(rows_inventario, columns=headers_inventario)
inventario_df.to_csv("Data/Inventario.csv", sep=";", index= True, index_label="Cons")