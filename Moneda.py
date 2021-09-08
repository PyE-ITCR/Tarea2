#Para el primer caso se selccionó el método de distribución VAD: Distribución Gométrica. Esto debido a que el mismo se centra en el objetivo
#Planteado, que es el número de ensayos que se deben llevar a cabo antes de conseguir un único éxito, siendo este que salga un escudo.

#Para el segundo caso se seleccionó el método de distribución VAD: Distribución Binominal Negativa, debido a los parámetros y descripción del
#mismo, pues el mismo encuentra la cantidad de ensayos que se deben realizar para conseguir N éxitos, que es el problema planteado.

#Una vez averiguada la cantidad de ensayos por éxito se debe construir la funcion de masa de probabilidad y graficar

from matplotlib import pyplot as plt

#Calcula el factorial de un numero
def factorial(num):
    resultado = 1
    while(num > 0):
        resultado = resultado * num
        num -= 1
    return resultado

def parte1(p):
    
    x = []
    y = []
    cont = 1
    
    while(cont <= 20):
        f = (1 - p)**(cont - 1) * p
        x.append(cont)
        y.append(f)
        cont += 1

    plt.stem(x, y)
    plt.title("Gráfico moneda ideal (Caso de exito: " + str(p) + ")")
    plt.xlabel('Ensayos')
    plt.ylabel('Probabilidad')
    plt.show()

def parte2(p):

    x = [1, 2]
    y = [0, 0]

    r = 3
    cont = 3

    while(cont <= 20):
        
        f = factorial(cont - 1)/(factorial(r-1)*factorial(cont-1-(r-1))) * (1 - p)**(cont - r) * p**r
        x.append(cont)
        y.append(f)
        cont += 1

    plt.stem(x, y)
    plt.title("Gráfico moneda trucada (Caso de exito: " + str(p) + ")")
    plt.xlabel('Temperatura')
    plt.ylabel('Probabilidad')
    plt.show()

parte1(0.5)
parte2(0.3)
    
