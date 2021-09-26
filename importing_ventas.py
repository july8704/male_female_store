import numpy as np
import pandas as pd

## Read the sale file
x = 0
with open("Data/Ventas.txt", "r") as archivo:
    headers = ""
    rows = list()
    for linea in archivo: #Run o analize each row
        if x == 0: # Extract titles or column's names
            letter_ant = ""
            y = 0
            for letter in linea: #Treating white spaces

                if letter != ' ' and letter_ant != ' ':
                    headers = headers + letter
                elif letter == ' ' and letter_ant != ' ':
                    headers = headers + letter
                elif letter != ' ' and letter_ant == ' ':
                    headers = headers + letter
                letter_ant = letter
                y = y + 1

            headers = headers.rstrip().split(' ')
        else: #Putting separator, ;.
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
            rows.append(row.strip().split(';'))

        x = 1 + x
ventas_df = pd.DataFrame(rows, columns= headers)
ventas_df.to_csv("Data/ventas.csv", sep=";", index= True, index_label="Cons")