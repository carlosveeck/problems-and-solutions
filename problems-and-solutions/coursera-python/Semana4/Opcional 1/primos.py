numero = int(input("Digite um número inteiro:"))
check = False
divisor = 2

while check == False and divisor < numero:
    resto = numero % divisor
    if resto == 0:
        check = True
    divisor = divisor + 1

if check == False:
    print("primo")
else:
    print("não primo")




