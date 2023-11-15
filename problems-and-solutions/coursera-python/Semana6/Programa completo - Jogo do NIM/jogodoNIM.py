def usuario_escolhe_jogada(n, m):
    user = int(input("faça sua jogada:"))
    valido = False
    while valido == False:
        if user <= m and user > 0:
            valido = True
        else:
            user = int(input("jogada inválida, faça outra jogada:"))

    return user


def computador_escolhe_jogada(n,m):
    maquina = m
    verifica = False
    while verifica == False:
        valor = (n - maquina)%(m+1)
        if valor == 0:
                verifica = True
        else:
                maquina = maquina - 1
    return maquina




def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    pecasAtuais = n
    while pecasAtuais > 0:
        if n%(m+1) != 0:
            if pecasAtuais == n:
                print("Computador começa!")
            pecasRetiradasPc = computador_escolhe_jogada(pecasAtuais,m)
            print("O computador tirou",pecasRetiradasPc,"peça(s).")
            print("restam",pecasAtuais-pecasRetiradasPc,"peças no tabuleiro")
            pecasAtuais = pecasAtuais - pecasRetiradasPc
            if pecasAtuais > 0:
                pecasRetiradasUser = usuario_escolhe_jogada(pecasAtuais,m)
                print("Você tirou",pecasRetiradasUser,"peça(s).")
                print("restam",pecasAtuais - pecasRetiradasUser,"peças no tabuleiro")
                pecasAtuais = pecasAtuais - pecasRetiradasUser
        else:
            if pecasAtuais == n:
                print("Voce começa!")
            pecasRetiradasUser = usuario_escolhe_jogada(pecasAtuais, m)
            print("Você tirou", pecasRetiradasUser, "peça(s).")
            print("restam", pecasAtuais - pecasRetiradasUser, "peças no tabuleiro")
            pecasAtuais = pecasAtuais - pecasRetiradasUser
            pecasRetiradasPc = computador_escolhe_jogada(pecasAtuais, m)
            print("O computador tirou", pecasRetiradasPc, "peça(s).")
            print("restam", pecasAtuais - pecasRetiradasPc, "peças no tabuleiro")
            pecasAtuais = pecasAtuais - pecasRetiradasPc
    print("Fim do jogo! O computador ganhou!")


def campeonato():
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")

start = 0
while start >= 3 or start <= 0:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    start= int(input())
    if start == 1:
        print("Você escolheu uma partida!")
        partida()
    elif start == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
    else:
        print("modo de jogo inválido, escolha um dos modos apresentados")
