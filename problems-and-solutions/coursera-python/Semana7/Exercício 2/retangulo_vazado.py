largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))
contadorL = 1
contadorA = 1

while contadorA <= altura:
    contadorL = 1
    while contadorL <= largura:
        if contadorL == largura and contadorA != altura:
            print("#")
        elif contadorA == 1 or contadorA == altura or contadorL == 1:
            print("#",end="")
        else:
            print(" ",end="")
        contadorL = contadorL + 1
    contadorA = contadorA + 1



