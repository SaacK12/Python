def es_bisiesto(year):
    if year % 100 == 0 and year % 400 == 0:
        print("El año introducido es bisiesto!")
    elif year % 100 == 0:
        print("El año introducido no es bisiesto.")
    else:
        print("El año introducido es bisiesto!")
año= int(input("Introduzca el año a comprobar: "))
es_bisiesto(año)