import math
x1 = int(input("Digite um valor para x1: "))
y1 = int(input("Digite um valor para y1: "))
x2 = int(input("Digite um valor para x2: "))
y2 = int(input("Digite um valor para y2: "))

horizontal = x2 - x1
vertical = y2 - y1
distancia = math.sqrt(vertical**2 + horizontal**2)

print("A distância entre os 2 pontos é",distancia,"unidades.")

