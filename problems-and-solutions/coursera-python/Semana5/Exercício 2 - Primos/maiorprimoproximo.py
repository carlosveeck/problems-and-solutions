def eh_primo(numero):  ##esta função devolve true pra primo e false pra não primo
    check = False
    divisor = 2

    while check == False and divisor < numero:
        resto = numero % divisor
        if resto == 0:
            check = True
        divisor = divisor + 1
    return (not check)

def maior_primo(x):
    if eh_primo(x) == True:
        return(x)
    else:
        while eh_primo(x) == False:
            x = x - 1
        return(x)


