import sqlite3
import random

def selecionar_palavra_aleatoria():
    coon = sqlite3.connect('lista_objetos.db')
    cursor = coon.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS palavras (
                    palavra TEXT
                    )''')

    # Ler palavras do arquivo txt e inserir na tabela
    with open('lista_objetos.txt', 'r') as arquivo:
        palavras = arquivo.readlines()
        for palavra in palavras:
            palavra = palavra.strip()  # Remover espaços em branco e quebras de linha
            cursor.execute("INSERT INTO palavras (palavra) VALUES (?)", (palavra,))

    # Selecionar palavras
    cursor.execute("SELECT palavra FROM palavras ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    palavra_aleatoria = row[0]

    coon.close()

    return palavra_aleatoria