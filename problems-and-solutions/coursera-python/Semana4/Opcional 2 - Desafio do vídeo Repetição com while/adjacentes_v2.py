numero = int(input("Digite seu número: "))

restoAnterior = numero % 10
numeroSobrou = numero // 10
restoAtual = numeroSobrou % 10
existeConsecutivo = False

while numeroSobrou != 0:
     if restoAtual == restoAnterior:
         print("Esse número possui algarismos consecutivos, representados por:",restoAtual)
         existeConsecutivo = True
     numeroSobrou = numeroSobrou//10
     restoAnterior = restoAtual
     restoAtual = numeroSobrou % 10


if existeConsecutivo == False:
    print("Não existem algarismos consecutivos neste número")