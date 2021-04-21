#importamos pandas para poder leer el archivo de excel que contiene los datos

import pandas as pd

#  Leemos el archivo y la hoja de excel con read_excel

df=pd.read_excel('Gráficas1.xlsx',sheet_name='Hoja1')

# Con .values leemos los datos de la columna 'x' y 'y'

valoresx=df['x'].values
valoresy=df['y'].values

# Imprimimos estos datos para comprobar que son una lista

print(valoresx)

# Importamos la libreria para graficar

import matplotlib.pyplot as plt

# Una variable que contiene los colores de las graficas que realizaremos

colores=['b','g','y']

# Con zip fusionamos las matrices de valores y colores, primer elemento de una con el primer elemento de la otra

for p,c in zip(valoresx,colores):

    # Graficamos las lineas verticales e insertamos una leyenda

    plt.axvline(p,  label='línea: {}'.format(p),c=c)


# Graficamos la leyenda

plt.legend()

# Guardamos la figura como un archivo .png

plt.savefig('grafica1.png')

# Ahora vamos a repetir el proceso pero con lineas horizontales

colores=['r','k','m']

for p,c in zip(valoresx,colores):

    grafica2=plt.axhline(p,  label='línea: {}'.format(p),c=c)
    
# La grafica se realizará sobre la anterior

plt.savefig('grafica2.png')

# Terminamos de graficar

plt.close()



# Vamos a hacer dos graficos en una figura



  # 1 fila, 2 columnas, indice 1

# Graficamos valores x contra valores y de color cian

plt.plot(valoresx,valoresy,color='c')

# Nombramos los ejes

plt.xlabel('Eje x1')

plt.ylabel('Eje y1')

# Creamos la segunda grafica

plt.subplot(1,2,2)

  # 1 fila, 2 columnas, indice 2

# Grafica de color magenta

plt.plot(valoresy,valoresx,color='m')

# Nombramos los ejes

plt.xlabel('Eje x2')

plt.ylabel('Eje y2')

# Guardamos la figura

plt.savefig('grafica3.png')

# Cerramos

plt.close()


# Leemos otra hoja del archivo que subimos anteriormente

df=pd.read_excel('Gráficas1.xlsx',sheet_name='Hoja2')

# Con .values leemos los datos de la columna 'x' 

x=df['x'].values

# Creamos unos vectores nuevos a partir del anterior

x2=x**2
x3=x**3

# Graficamos 3 curvas en la misma figura

plt.plot(x, x, 'b.', x, x2, 'rd', x, x3, 'g^')

  # b. puntos azules, rd diamantes delgados rojos, g^ triagulos hacia arriba verdes

plt.savefig('grafica4.png')

plt.close()



# Se importan tadas las funciones de math y numpy

from math import *
from numpy import *

# Se leen los valores de la columna y de la hoja2 de graficos1

y=df['y'].values

# Grafico de funciones

y1=log10(y)*sin(y)
y2=sin(y)*exp(-y)

# Graficamos ambas funciones una -.k linea a puntos y rayas negra, :y linea punteada roja

plt.plot(y,y1,'-.k',y,y2,':r')

# Agregamos texto dentro de las graficas en las coordenadas (2,0.6) y (10,0.5)

plt.text(7, 1, r'y1=ln(x)sin(x)', fontsize=10)
plt.text(6.5, -0.3, r'y2=$\sin(x) \cdot e^{-x}$', fontsize=10)

# Malla

plt.grid()

# Ingresamos los nombres de los ejes y de la figura

plt.title('Grafica de funciones')
plt.xlabel('eje x')
plt.ylabel('ejey')

# Vamos a ubicar y graficar un punto de la grafica

xx=2
yy=log10(xx)*sin(xx)

# Graficamos el punto azul 'bo'

plt.plot([xx],[yy],'bo')

# Ahora haremos una señalización del punto

plt.annotate(r'ln(2)sin(2)=0.024',xy=(xx,yy),xycoords='data',xytext=(2,0.5),fontsize=8,arrowprops=dict(arrowstyle='->'))

plt.savefig('grafica5.png')

plt.close()




# Crear un histograma 

plt.subplot(2,2,1)
plt.hist(x)

# Grafica de dispersión


x1=sqrt(x)
x2=x+y**2

plt.subplot(2,2,2)
plt.scatter(x1,x2)

# Grafico de barras

y1=(0.5+x)**2
y2=(0.5-x)**2

plt.subplot(2,2,3)

  # En la misma grafica una hacia arriba y otra hacia abajo

plt.bar(x, +y1, facecolor='r')
plt.bar(x, -y2, facecolor='y')

# Escribimos el porcentaje que representa cada barra

for x, y in zip(x, y1):
    plt.text(x + 0.4, y + 0.05, '%.1f' % y, ha='center', va='bottom')



plt.savefig('grafica6.png')

plt.close()









