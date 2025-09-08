import math
def stupidMathForm(dolar,int, año):
    inter= math.pow((1+int/100),año)
    resultado= dolar * inter
    print(resultado)
dolares= float(input("Introduzca una cantidad de dolares"))
tasaDeInteres= float(input("Introduzca la tasa de interes"))
años= float(input("Introduzca el numero de años"))
stupidMathForm(dolares,tasaDeInteres,años)