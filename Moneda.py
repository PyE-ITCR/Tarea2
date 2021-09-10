#Para el primer caso se selccionó el método de distribución VAD: Distribución Gométrica. Esto debido a que el mismo se centra en el objetivo
#Planteado, que es el número de ensayos que se deben llevar a cabo antes de conseguir un único éxito, siendo este que salga un escudo.

#Para el segundo caso se seleccionó el método de distribución VAD: Distribución Binominal Negativa, debido a los parámetros y descripción del
#mismo, pues el mismo encuentra la cantidad de ensayos que se deben realizar para conseguir N éxitos, que es el problema planteado.

#Una vez averiguada la cantidad de ensayos por éxito se debe construir la funcion de masa de probabilidad y graficar

from matplotlib import pyplot as plt
import math as mt

#Calcula el factorial de un numero
def factorial(num):
    resultado = 1
    while(num > 0):
        resultado = resultado * num
        num -= 1
    return resultado

#Funcion para parte 1
def parte1(p):
    
    x = [] #Lista de ensayos
    y = [] #Lista de probabilidades
    cont = 1 #Contador de ensayos

    #Loop que calcula los valores de la función de masa de probabilidad por ensayos
    while(cont <= 20):
        
        f = (1 - p)**(cont - 1) * p #Función masa de probabilidad para Distribución Geométrica
        x.append(cont) #Se añade el número de ensayo a la lista de ensayos
        y.append(f) #Se añade el valor de la función de masa de probabilidad a la lista de probabilidades
        cont += 1 #Aumenta ensayos

    media = 1/p #Se calcula la media para la Distribución Geométrica
    varianza = (1 - p)/p**2 #Se calcula la varianza para la Distribución Geométrica
    desvEst = mt.sqrt(varianza) #Se calcula la desviación estándar para la Distribución Geométrica

    #Se define la fuente para los textos en pantalla
    font = {'family': 'serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 14,
        }

    #Se definen los valores y el tipo de gráfica a ejecutar
    plt.stem(x, y)
    plt.title("Gráfico distribución geométrica (Caso de exito: " + str(p) + ")")
    plt.text(14, 0.44, "Media = " + str(round(media, 2)), fontdict=font)
    plt.text(14, 0.40, "Varianza = " + str(round(varianza,2)), fontdict=font)
    plt.text(14, 0.36, "Desv Est = " + str(round(desvEst, 2)), fontdict=font)
    plt.xlabel('Ensayos')
    plt.ylabel('Probabilidad')
    plt.subplots_adjust(left=0.15)
    plt.show()

    

#Funcion para parte 2
def parte2(p):

    x = [1, 2] #Lista de ensayos
    y = [0, 0] #Lista de probabilidades

    r = 3 #Número de éxtios
    cont = 3 #Contador de ensayos

    #Loop que calcula los valores de la función de masa de probabilidad por ensayos
    while(cont <= 20):
        
        f = factorial(cont - 1)/(factorial(r-1)*factorial(cont-1-(r-1))) * (1 - p)**(cont - r) * p**r #Función masa de probabilidad para Distribución Binominal Negativa
        x.append(cont) #Se añade el número de ensayo a la lista de ensayos
        y.append(f) #Se añade el valor de la función de masa de probabilidad a la lista de probabilidades
        cont += 1 #Aumenta ensayos

    media = r/p #Se calcula la media para la Distribución Binominal Negativa
    varianza = r**(1 - p)/p**2 #Se calcula la varianza para la Distribución Binominal Negativa
    desvEst = mt.sqrt(varianza) #Se calcula la desviación estándar para la Distribución Binominal Negativa

    #Se define la fuente para los textos en pantalla
    font = {'family': 'serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 14,
        }

    #Se definen los valores y el tipo de gráfica a ejecutar
    plt.stem(x, y)
    plt.title("Gráfico distribución binomial negativa (Caso de exito: " + str(p) + ")")
    plt.text(15, 0.095, "Media = " + str(media), fontdict=font)
    plt.text(13.5, 0.088, "Varianza = " + str(round(varianza, 2)), fontdict=font)
    plt.text(14.5, 0.081, "Desv Est = " + str(round(desvEst,2)), fontdict=font)
    plt.xlabel('Ensayos')
    plt.ylabel('Probabilidad')
    plt.subplots_adjust(left=0.15)
    plt.show()

parte1(0.5)
parte2(0.3)
    
