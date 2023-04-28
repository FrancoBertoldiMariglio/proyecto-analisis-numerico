from matplotlib import pyplot as plt
import argparse
import numpy as np
from tabulate import tabulate

# Esta es la funcion dy/dx


def yprime(x, y):
    # return 4*math.e**(0.8*x) - 0.5*y
    # return np.log(y)
    return np.sin(x*y)

# Este es el programa que calcula la tabla de valores para x, y & f(x,y)


def euler(intMin=-4, intMax=4, dist=0.1, x0=-4, y0=2):

    # Definimos variables y listas
    xList = [x0]
    yList = [y0]
    fxyList = []
    rango = int((intMax-intMin)*(1/dist) + 1)
    cont = 1
    arr = [["Iteracion", "x", "y", "f(x,y)"]]
    list = np.array(arr)

    for i in range(rango):

        # En la primera iteracion agregamos a la lista los valores iniciales para x (x0), y (y0) y calculamos f(x,y)0
        if i == 0:
            list = np.append(list, np.array(
                [[cont, x0, y0, yprime(x0, y0)]]), axis=0)
            xList.append(xList[i] + dist)
            yList.append(yList[i] + dist*yprime(xList[i], yList[i]))
            fxyList.append(yprime(xList[i], yList[i]))
            continue

        # Esta condicion se asegura que los valores de x lleguen hasta el numero maximo de x del dominio proporcionado
        if float(list[i][1]) >= intMax:
            break

        # Aca agregamos los nuevos xn, y yn f(x,y)n
        cont += 1
        list = np.append(list, np.array([[cont,
                                          float(list[i][1]) + dist,
                                          float(list[i][2]) + dist*yprime(float(list[i][1]), float(list[i][2])),
                                          yprime(float(list[i][1]), float(list[i][2]))]]),
                         axis=0)
        if i < rango-1:
            xList.append(xList[i] + dist)
            yList.append(yList[i] + dist*yprime(xList[i], yList[i]))
            fxyList.append(yprime(xList[i], yList[i]))


    # Imprimimos por pantalla la tabla de valores
    print(tabulate(list[1:], headers=list[0]))

    # Grafica los valores de la tabla
    plt.plot(xList[:-1], yList[:-1], color='black')
    plt.plot(xList[:-1], yList[:-1], 'o', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.title(f'Solucion a dy/dx = 4*math.e**(0.8*x) - 0.5*y')
    # plt.title(f'Solucion a dy/dx = np.log(y))
    # plt.title(f'Solucion a dy/dx = np.sin(x*y))
    plt.show()


if __name__ == '__main__':
    # parseador
    parser = argparse.ArgumentParser()
    parser.add_argument("-min", type=float, help="limite inferior del intervalo")
    parser.add_argument("-max", type=float, help="limite superior del intervalo")
    parser.add_argument("-dist", type=float, help="saltos entre cada punto")
    parser.add_argument("-x0", type=float, help="valor inicial de x")
    parser.add_argument("-y0", type=float, help="valor inicial de y")
    args = parser.parse_args()
    
    # funcion
    euler(intMin=args.min, intMax=args.max, dist=args.dist, x0=args.x0, y0=args.y0)
