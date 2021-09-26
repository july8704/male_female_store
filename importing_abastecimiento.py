import numpy as np
import pandas as pd

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
        x = x+1
    pd_inventario = pd.DataFrame(data=abastecimiento_list, columns=head.split(" "))
    pd_inventario.to_csv("Data/Abastecimiento.csv", sep = ";", index= True, index_label="Cons")