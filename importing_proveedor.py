import numpy as np
import pandas as pd

pd_proveedores = pd.read_excel ("Data/Proveedores.xlsx")
pd_proveedores.to_csv("Data/Proveedores.csv", sep = ";", index= True, index_label= "Cons")