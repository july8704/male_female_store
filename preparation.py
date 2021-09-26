import numpy as np
import pandas as pd

## Read the sale file
def read_ventas ():
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

    return ventas_df

# Reading Products data

def read_product ():
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
                        if delimiter == False:
                            row = row + ";"
                        delimiter = True
                        # row.append(rows)
                    else:
                        row = row + letter
                        delimiter = False
                    letter_ant = letter
                if len(row.strip().split(';')) == 5:
                    rows = row.strip().split(';')
                    rows.pop(4)
                    rows_producto.append(rows)
                else:
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
    productos_df.to_csv("Data/Productos.csv", sep=";", index=True, index_label="Cons")

    return productos_df

# Reading Inventory data

def inventory ():
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
                        if delimiter == False:
                            row = row + ";"
                            delimiter = True
                    else:
                        # row.append(rows)
                        row = row + letter
                        delimiter = False
                    letter_ant = letter
                row = row.replace('00:00:00.000', '00:00:00.000;')
                rows_inventario.append(row.strip().split(';'))
            x = 1 + x
        inventario_df = pd.DataFrame(rows_inventario, columns=headers_inventario)
    inventario_df.to_csv("Data/Inventario.csv", sep=";", index=True, index_label="Cons")

    return inventario_df

# Reading Abastecimiento

def read_abastecimiento ():
    with open("Data/Abastecimiento.txt") as archivo:
        abastecimiento_list = list()
        head = list()
        x = 0
        for line in archivo:

            lineline = " ".join(line.split())
            lineline = lineline.strip()
            if x == 0:
                head = lineline
            else:
                abastecimiento_list.append(lineline.split(" "))
            x = x + 1
        pd_abastecimiento = pd.DataFrame(data=abastecimiento_list, columns=head.split(" "))
        pd_abastecimiento.to_csv("Data/Abastecimiento.csv", sep=";", index=True, index_label="Cons")
        return pd_abastecimiento
# Reading proveedores

def read_proveedores ():
    pd_proveedores = pd.read_excel("Data/Proveedores.xlsx")
    pd_proveedores.to_csv("Data/Proveedores.csv", sep=";", index=True, index_label="Cons")
    return  pd_proveedores


