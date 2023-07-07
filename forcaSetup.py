from selecionarPalavra import selecionar_palavra_aleatoria
import os

def jogar_novamente():
    jogarNovamente = input("Para jogar novamente digite 1 \n")
    if jogarNovamente == '1':
        jogar_forca()

#montar a forca

def montar_forca(palavra, letras_erradas, letras_corretas, palavra_montada):
    forca = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========='''
    ]

    # Montar a representação visual da forca
    indice_forca = len(letras_erradas)
    if indice_forca > 5:
        indice_forca = 6
    desenho_forca = forca[indice_forca]

    # Montar a palavra com as letras adivinhadas e traços para as letras não adivinhadas
    palavra_montada = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_montada += letra
        else:
            palavra_montada += '_'

    # Exibir a forca e a palavra atual
    print(desenho_forca)
    print('Palavra:', palavra_montada)

def jogar_forca():
    palavra_secreta = selecionar_palavra_aleatoria()
    letras_erradas = []
    letras_corretas = []
    palavra_montada = ''

    while True:
        montar_forca(palavra_secreta, letras_erradas, letras_corretas, palavra_montada)

        palavra_montada = ''
        for letra in palavra_secreta:
            if letra in letras_corretas:
                palavra_montada += letra
            else:
                palavra_montada += '_'
    
        if '_' not in palavra_montada:
            print("Parabéns! Você venceu!")
            jogar_novamente()
            break

        letra = input("Digite uma letra: ").lower()

        if letra in letras_erradas or letra in letras_corretas:
            print("Você já utilizou essa letra. Tente uma diferente.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
        else:
            letras_erradas.append(letra)

        if len(letras_erradas) > 5:
            print("Você perdeu! A palavra secreta era: ", palavra_secreta)
            jogar_novamente()
            break


jogar_forca()