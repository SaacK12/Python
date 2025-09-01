frase= input("Introduzca una frase: ")
vocal= input("Introduzca una vocal: ")
while vocal not in "aeiou":
    vocal = input("Vocal no valida. Vuelva a intentarlo: ")
fraseModificada = frase.replace(vocal, vocal.upper())
print(fraseModificada)