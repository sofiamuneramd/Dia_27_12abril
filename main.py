#importamos pandas para poder leer el archivo de excel que contiene los datos

import pandas as pd

df=pd.read_excel('Gráficas1.xlsx',sheet_name='Hoja1')

valores=df['x'].values

print(valores)

import matplotlib.pyplot as plt

for p in valores:

    plt.axvline(p,  label='línea vertical')

plt.legend()

grafica1=plt.show()

from pandas import ExcelWriter

file=ExcelWriter('Copia1.xlsx')
grafica1.to_excel(file,'Hoja1')
file.save()