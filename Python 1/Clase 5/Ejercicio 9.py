cantidadAInvertir= float(input("¿Cuanto es la cantidad que desea invertir? "))
interesAnual= float(input("Ingrese un interes anual (%): "))
numeroAnual= float(input("Ingrese el numero de años: "))
capitalFinal= cantidadAInvertir*(1 + interesAnual/100)**numeroAnual
capitalFinal= round(capitalFinal,2)
print("El capital final obetnido es de: ",capitalFinal)