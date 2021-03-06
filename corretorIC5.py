from spellchecker import SpellChecker
from nltk.tokenize import RegexpTokenizer

from nltk.tokenize import LineTokenizer

with open('relatosSemRepeticao.txt', 'r', encoding='utf-8') as text_file:   #abre o arquivo com encoding utf-8
    str = text_file.read()  #transforma o texto em string

f = open("relatosCorrigido.txt", "w")

#print(str)

#divide o string 'lista' em um sub-string
substring = []
char = ""
num = ""
for letter in str:
    if letter.isdigit():
        if char:
            substring.append(char)
            char = ""
        if letter == "+":
            num += "5"
        if letter == "\n":             
            num += " 15978 "         
        else:
            num += letter
    else:
        if num:
            substring.append(num)
            num = ""
        if letter == "+":
            char += "5"
        if letter == "\n":                        
            char += " 15978 "            
        else:
            char += letter

substring.append(char) if char else substring.append(num)

#print(substring)

str2 = ' '.join(substring)   #transforma a lista substring em string str2

tokenizer = RegexpTokenizer(r'\w+')     #tokenizer do nlkt
lista = tokenizer.tokenize(str2)        #string tokenizado em lista

#print(lista)    #imprime a lista para debug

with open('automoveis.txt', 'r', encoding='utf-8') as text_file:   #abre o arquivo com encoding utf-8
    str = text_file.read()  #transforma o texto em string

#f = open("erros.txt", "w")

#print(str)

#divide o string 'lista' em um sub-string com os numeros separados
substring = []
char = ""
num = ""
for letter in str:
    if letter.isdigit():
        if char:
            substring.append(char)
            char = ""
        num += letter
    else:
        if num:
            substring.append(num)
            num = ""
        char += letter
substring.append(char) if char else substring.append(num)
#print(substring)   #imprime o string com substrings gerado para debug

str2 = ' '.join(substring)   #transforma a lista substring em string str2

listaAuto = tokenizer.tokenize(str2)        #string tokenizado em lista

#print(listaAuto)

#unknown = flat_list
spell = SpellChecker(language='pt')     #cria objeto do tipo SpellChecker em portugues

#adiciona nomes pr??prios ao dicionario
spell.word_frequency.load_words(listaAuto)

#adiciona nomes pr??prios ao dicionario
spell.word_frequency.load_words(['Douglas', 'Felippe', 'Stefanio', 'Am??lia', 'Miguel', 'Arthur', 'Davi', 'Gabriel', 'Maria Eduarda', 'Alice', 'Heitor', 'Pedro', 'Laura', 'Douglas', 'Joaquim', 'Queiroz'])

#adiciona abreviacoes
spell.word_frequency.load_words(['demais','mp', 'fb', 'jr', 'hd', 'j??', 'V??rias', 'v??rias', 'm??xima', 'pres??dio', 'pe??o', 'cab??veis', 'den??ncia', 'amedrontando', 'hilux', 'niter??i', 'oce??nica', 'tr??fico'])

#adiciona ao lexico
spell.word_frequency.load_words(['omissa', 'botelho', 'itaquera', 'hidr??metro', 'boleto', 'caveirao', 'carioca', 'guanabara', 'acuado', 'atuem', 'maciel', 'macumba', 'rog??rio', 'coibir', 'ourique', 'cacheado', 'suzano', 'mercadao', 'favelinha', 'mauricio', 'cai??ara', 'maicon'])

#abreviacoes = ["cv", "mp", "bpm", "av", "melissa", "sao", "Mel??cia", "mto", "Melissa", "oq", "d+", "Pfv", "q", "??"]
#significados = ["comando vermelho", "minist??rio p??blico", "batalh??o da pol??cia militar", "avenida", "mil??cia", "s??o", "mil??cia", "muito", "mil??cia", "o que", "demais", "por favor", "que", "n??o"]

import csv

with open('internetes.txt', encoding='utf-8-sig') as arq_csv:   # verificar se o arquivo .txt esta sem espacos em branco!
    table = csv.reader(arq_csv, delimiter=',')  # lendo a tabela

    abr = {}  # Criando dicion??rio

    for row in table:  # Iterando sobre ele
        abr[row[0]] = row[1]
        
with open('seguranca.txt', encoding='utf-8-sig') as arq_csv2:   # verificar se o arquivo .txt esta sem espacos em branco!
    table2 = csv.reader(arq_csv2, delimiter=',')  # lendo a tabela    
    
    #abr = {}  # Criando dicion??rio    
    
    for row in table2:  # Iterando sobre ele
        abr[row[0]] = row[1]        


repeticoes = ["aaa", "eee", "iii", "ooo", "uuu"] # lista para eliminacao de repeticoes de letras

for word in lista:
    #if word in abreviacoes: # transforma as abreviacoes da lista em seu significado
    #    word = significados[abreviacoes.index(word)]                                   # nao funciona dentro deste loop
    
    for i in repeticoes: # procura por letras repetidas como na lista 'repeticoes' e elimina repeticao
        if i in word:
            lista[lista.index(word)] = ''.join(sorted(set(word), key=word.index))

#print(abr.keys())
#print (spell.known(misspelled))    # Returns those words that are in the word frequency list
#print (spell.unknown(misspelled))  # Returns those words that are not in the frequency list

listaMaiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#palavrasMaiusculas = []

for word in lista:
    if word in abr.keys(): # transforma as abreviacoes da lista em seu significado        
        f.write(abr[word])
        f.write(" ")
    elif word == "15978":
        f.write("\n")
    
    else:
        f.write(spell.correction(word))
        f.write(" ")
        
    #if word[0] in listaMaiusculas:
    #    palavrasMaiusculas.append(word)        

    
    
#print(palavrasMaiusculas)