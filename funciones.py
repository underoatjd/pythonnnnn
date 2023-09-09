def sumas_valores(*args):
    resultado=0
    for valor in args:
        resultado+=valor
    return resultado      

print(sumas_valores(3,5,9,8,9,6,3,2,5,48,7,4,5,6,2,1,4,7,9))
