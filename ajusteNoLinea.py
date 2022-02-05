import matplotlib.pyplot as plt
import numpy as np
from fit_leastsq import fit_leastsq

#Cargar los datos
x_exp, y_exp = np.loadtxt(fname="el nombre del archivo.csv", delimiter=",", unpack=True)

#Definir la funcion de ajuste
#Esto es solo un ejemplo no me acuerdo en este mometo cual es la funcion.
#p0, p1, p2 son los parametros de ajuste. Se pueden agragar mas o quitar.
funcF = lambda x, p0, p1, p2: p0 * np.sin(p1 * x) + p2 #Aqui se define la funcion manualmente
funcFF = lambda x, p: funcF(x, *p) 

#Realizar el ajuste

#parametros iniciales
pstart = [0, 1, 2]
pfit, perr = fit_leastsq(pstart, x_exp, y_exp, funcFF)

#Parametros de ajuste
p0, p1, p2 = pfit

#Sus errores
Dp0, Dp1, Dp2 = perr

#Imprimir resultados en la consola
print(pfit)
print(perr)

#Realizar la grafica

#Generar datos de la curva toerica
x_teo = np.linspace(-4, 4, 100)  #Los parametros de esta funcion especifican el numero el intervalo y el numero de datos
y_teo = funcFF(x_teo, pfit)

#Graficar el ajuste junto con los datos experimentales
plt.plot(x_exp, y_exp, '*', label = "El nombre que quieras") 
plt.plot(x_teo, x_teo, '--', label = "El nombre que quieras") 
plt.grid() #Le coloca la grilla
plt.legend() #Coloca las leyendas
plt.show()
plt.savefig("El nombre que quieras.png")
