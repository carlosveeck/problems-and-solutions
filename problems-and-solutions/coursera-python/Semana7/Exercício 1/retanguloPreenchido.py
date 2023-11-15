largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))
contadorL = 1
contadorA = 1

while contadorA <= altura:
    contadorL = 1
    contadorA = contadorA + 1
    while contadorL <= largura:
        print("#",end="")
        if contadorL == largura and contadorA <= altura:
            print("")

        contadorL = contadorL + 1
