import math
A = int(input("Informe um valor para A: "))
B = int(input("Informe um valor para B: "))
C = int(input("Informe um valor para C: "))
delta = (B**2) - (4*A*C)
if delta < 0:
    print("esta equação não possui raízes reais")
elif delta >= 0:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    if x1 = x2
       print("a raiz desta equação é",x1)
    elif x2 < x1:
        print("as raízes da equação são",x2,"e",x1)
    else:
        print("as raízes da equação são",x1,"e",x2)
