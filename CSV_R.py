'''
Para adicionar qualquer abreviação colocar no arquivo internetes.txt. EX:

            abreviação, palvara
            cv,comando vermelho

'''
import csv

with open('internetes.txt', encoding='utf-8-sig') as arq_csv:
    table = csv.reader(arq_csv, delimiter=',')  # lendo a tabela

    abr = {}  # Criando dicionário

    for row in table:  # Iterando sobre ele
        abr[row[0]] = row[1]

print(abr)
