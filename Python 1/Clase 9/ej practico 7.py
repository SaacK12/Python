def esPalindromo(stg):    
    stg = stg.lower()
    if stg == stg[::-1]:
        palindromo= True
        print(palindromo)
    else:
        palindromo= False
        print(palindromo)
palabra= input("Introduce un texto:")
esPalindromo(palabra)