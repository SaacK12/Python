import time
def convertirSegundos(sgd): #Con numeros demasiados grandes se demorara 
    segundo= sgd
    minutos= 0
    horas= 0
    while True:
        if segundo >= 60:
            segundo -= 60
            minutos += 1
            if minutos >= 60:
                minutos -= 60
                horas += 1
        else:
            break
    if horas < 10:
        horas= "0"+ str(horas)
    if minutos < 10:
        minutos= "0"+ str(minutos)
    if segundo < 10:
        segundo= "0"+ str(segundo)
    print(horas,":",minutos,":",segundo)

def cargando():
    time.sleep(1)
    print("Now loading...")
segundos= int(input("Introduzca segundos que sea convertir a horas y minutos: "))
convertirSegundos(segundos)