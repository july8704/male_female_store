import numpy as np
import pandas as pd

## Lectura del archivo de ventas
x = 0
with open("Data/Ventas.txt", "r") as archivo:
    headers = ""
    rows = list()
    for linea in archivo:
        if x == 0:
            letter_ant = ""
            y = 0
            for letter in linea:

                if letter != ' ' and letter_ant != ' ':
                    headers = headers + letter
                elif letter == ' ' and letter_ant != ' ':
                    headers = headers + letter
                elif letter != ' ' and letter_ant == ' ':
                    headers = headers + letter
                letter_ant = letter
                y = y + 1

            headers = headers.rstrip().split(' ')
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
            rows.append(row.strip().split(';'))

        x = 1 + x
ventas_df = pd.DataFrame(rows, columns= headers)

# Lectura del archivo de productos
x = 0
with open("Data/Productos.txt", "r") as archivo:
    headers_producto = ""
    rows_producto = list()
    for linea in archivo:
        linea   = linea.strip()
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
            rows_producto.append(row.strip().split(';'))

        x = 1 + x
productos_df = pd.DataFrame(rows_producto, columns=headers_producto)

# AGREGAR CLASIFICACION DEL PRODUCTO

#confitionlist = [
#    ('Mountain-500' == productos_df[['ProductModel']]),
#    ('Road' in productos_df['ProductModel']),
#    ('Touring' in productos_df['ProductModel']),
#    ('Classic' in productos_df['ProductModel'])]
#choicelist = ['Mountain', 'Road', 'Touring', 'Classic']
#productos_df['Clasification'] = np.select(confitionlist, choicelist, default='Not Specified')

#productos_df['Clasification'] = np.where(productos_df['ProductModel'].str.find('Mountain-500') != -1, 'Si', 'No')
#productos_df ['Clasification'] = productos_df['ProductModel'].str.strip() == 'Mountain-500'
productos_df ['Clasification'] = type(productos_df['ProductModel'].str)

for i in productos_df['Clasification']:
    print (i)
    #if i['ProductModel'].find('Mountain-500') != -1:
    #    print(str(productos_df['ProductModel']))
    #else:
    #    print("No especificado")

# Lectura del archivo de inventario
x = 0
with open("Data/Inventario.txt", "r") as archivo:
    headers_inventario = ""
    rows_inventario = list()
    for linea in archivo:
        linea = linea.strip()
        if x == 0:
            headers_inventario = linea.split()
            print(headers_inventario)
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
    #print(rows_inventario)
    inventario_df = pd.DataFrame(rows_inventario, columns=headers_inventario)
    #print(inventario_df)