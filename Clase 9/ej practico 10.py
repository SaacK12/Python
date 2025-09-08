def procedimiento(list):
    listaEnteros= (list.split())
    for n in listaEnteros:
        cantidad= int(n)
        histograma= ""
        for _ in range(cantidad):
            histograma += "*"
        print(histograma)
        
string= input("Introduzca una serie de numeros enteros separados por un espacio: ")
procedimiento(string)