import re
import math

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)





def calcula_assinatura(texto):
    lista_de_sentencas = separa_sentencas(texto)  #devolve lista de sentenças

    total_sentencas = len(lista_de_sentencas)

    caracteres_sentenca = 0
    lista_de_frases = []        ##lista contendo listas de frases e caracteres por sentença
    for sentenca in lista_de_sentencas:
        lista_de_frases.append(separa_frases(sentenca))
        caracteres_sentenca = caracteres_sentenca + len(sentenca)

    lista_de_palavras = []
    for frase in lista_de_frases:
        for x in range(len(frase)):
            lista_de_palavras.append(separa_palavras(frase[x]))


    total_palavras = 0
    total_letras = 0
    for list in lista_de_palavras:            ##cálculo da quantidade de letras e palavras no texto
        for obj in range(len(list)):
            palavra = list[obj]
            total_palavras = total_palavras + 1
            total_letras = total_letras + len(palavra)

    todas_palavras=[]
    for list in lista_de_palavras:
        for x in range(len(list)):
            todas_palavras.append(list[x])

    palavras_unicas = n_palavras_unicas(todas_palavras)  ##devolve número de palavras únicas

    palavras_diferentes = n_palavras_diferentes((todas_palavras)) ##devolve número de palavras diferentes

    total_frases = 0
    caracteres_frase = 0
    for frase in lista_de_frases:  ##devolve o total de frases
        for y in frase:
            total_frases = total_frases + 1
            caracteres_frase = caracteres_frase + len(y)

    wal_a = total_letras/total_palavras
    ttr_a = palavras_diferentes/total_palavras
    hlr_a = palavras_unicas/total_palavras
    sal_a = caracteres_sentenca/total_sentencas
    sac_a = total_frases/total_sentencas
    pal_a = caracteres_frase/total_frases



    #print("lista de sentenças:",lista_de_sentencas)
    #print("frases:",lista_de_frases)
    #print("palavras:",lista_de_palavras)
    #print("total palavras:",total_palavras)
    #print("total letras:",total_letras)
    #print("palavras unicas:",palavras_unicas)
    #print("palavras dif:",palavras_diferentes)
    #print("total sentenças:",total_sentencas)
    #print(caracteres_sentenca)
    #print(total_frases)
    #print(caracteres_frase)

    #print("wal",wal)
    #print("ttr",ttr)
    #print("hlr",hlr)
    #print("sal",sal)
    #print("sac",sac)
    #print("pal",pal)

    return [wal_a, ttr_a, hlr_a, sal_a, sac_a, pal_a]


def compara_assinatura(as_a, as_b):
    similaridade = 0
    for parametro in range(len(as_a)):
        similaridade = similaridade + abs(as_a[parametro] - as_b[parametro])

    return similaridade/6

def avalia_textos(textos, ass_cp):
    similaridades = []
    for texto in textos:
        similaridades.append(compara_assinatura(calcula_assinatura(texto),ass_cp))
    menor_numero = similaridades[0]
    menor_posicao = 0
    for x in range(len(similaridades)):
        if similaridades[x] < menor_numero:
            menor_posicao = x
            menor_numero = similaridades[x]

    return menor_posicao + 1












texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
print(calcula_assinatura(texto))

texto1 = " Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma."
texto2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
texto3 = "Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens."
textos = [texto1, texto2, texto3]
print(avalia_textos(textos,calcula_assinatura(texto)))

