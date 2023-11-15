n = int(input("Digite um número inteiro:"))
soma = 0
numero = n

while numero != 0:
    resto = numero % 10
    numero = numero // 10
    soma = soma + resto

print(soma)


