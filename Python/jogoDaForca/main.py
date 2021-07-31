from random import randint

corpo = [
    '''
        +-----+
        |     |
              |
              |
              |
              |
              |
              |
    ===========''',
    '''
        +-----+
        |     |
        o     |
              |
              |
              |
              |
              |
    ===========''',
    '''
        +-----+
        |     |
        o     |
       /|     |
              |
              |
              |
              |
    ===========''',
    '''
        +-----+
        |     |
        o     |
       /|\    |
              |
              |
              |
              |
    ===========''',
    '''
        +-----+
        |     |
        o     |
       /|\    |
       /      |
              |
              |
              |
    ===========''',
    '''
        +-----+
        |     |
        o     |
       /|\    |
       / \    |
              |
              |
              |
    ==========='''
]

palavras = ['bailarina', 'futebol', 'estatua', 'pintor', 'frio', 'lapis',
            'livro', 'astronauta', 'ator', 'cadeira', 'sacola', 'calculadora',
            'policial', 'amargo', 'xadrez', 'banana', 'pescador', 'semente'
            ]


def getPalavras(pLista):
    pIndex = randint(0, len(pLista) - 1)
    return pLista[pIndex]


def display(corpo, letraErrada, letraCorreta, palavraSecreta):
    print(corpo[len(letraErrada)])
    print()

    print('\033[7;31mLetras erradas -> \033[m ', end='')

    for letra in letraErrada:
        print(letra, end=' ')
    print()

    lacuna = '_ ' * len(palavraSecreta)

    # substituindo os espaços em branco pelas letras corretas.
    for cont in range(len(palavraSecreta)):
        if palavraSecreta[cont] in letraCorreta:
            lacuna = lacuna[:cont] + palavraSecreta[cont] + lacuna[cont + 1:]

    # mostrar a palavra secreta com espaços entre cada letra
    for letra in lacuna:
        print(letra, end=' ')
    print()


def get_chute(letraChute):
    """
    Garante que o usuário insira apenas uma letra.
    :param letraChute:
    :return: Letra escolhida pelo usuário
    """

    while True:
        chute = str(input('Chute: ')).lower().strip()

        if len(chute) != 1:
            print(f'\033[7;31mPor favor, digite apenas uma letra!\033[m')
        elif chute in letraChute:
            print(f'\033[7;32mAhh, essa você já chutou! Tente outra...\033[m')
        elif chute not in 'abcdefghijklmnopqrstuvwxyz':
            print(f'\033[7;31mPor favor, digite uma letra!\033[m')
        else:
            return chute


def jogarNovamente():
    return input('Jogar mais uma? Tecle S para sim ou [N] para não: ').lower().startswith('s')


print('-- C A R R A S C O --')
letraErrada = ''
letraCorreta = ''
palavraSecreta = getPalavras(palavras)
jogoFim = False

while True:
    display(corpo, letraErrada, letraCorreta, palavraSecreta)

    chute = get_chute(letraErrada + letraCorreta)

    if chute in palavraSecreta:
        letraCorreta = letraCorreta + chute
        pCompleta = True

        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] not in letraCorreta:
                pCompleta = False
                break

        if pCompleta:
            print(f'\033[33m\nLegal, a palavra secreta é:\033[m {palavraSecreta}')
            jogoFim = True

    else:
        letraErrada = letraErrada + chute

        if len(letraErrada) == len(corpo) - 1:
            display(corpo, letraErrada, letraCorreta, palavraSecreta)

            print(f'\033[34m\nQue pena, suas chances acabaram...\n'
                  f'Total de chutes errados: {len(letraErrada)}\n'
                  f'Total de chutes corretos: {len(letraCorreta)}\n'
                  f'Ahh, a palavra secreta era: {palavraSecreta}')
            jogoFim = True

    # verificar se o jogador que jogar novamente...
    if jogoFim:
        if jogarNovamente():
            letraErrada = ''
            letraCorreta = ''
            jogoFim = False
            palavraSecreta = getPalavras(palavras)
        else:
            break
