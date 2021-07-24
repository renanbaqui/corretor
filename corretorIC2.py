from spellchecker import SpellChecker
from nltk.tokenize import RegexpTokenizer

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
        num += letter
    else:
        if num:
            substring.append(num)
            num = ""
        char += letter
substring.append(char) if char else substring.append(num)
#print(substring)

str2 = ' '.join(substring)   #transforma a lista substring em string str2

tokenizer = RegexpTokenizer(r'\w+')     #tokenizer do nlkt
lista = tokenizer.tokenize(str2)        #string tokenizado em lista

#print(lista)    #imprime a lista para debug

#unknown = flat_list
spell = SpellChecker(language='pt')     #cria objeto do tipo SpellChecker em portugues

#adiciona nomes próprios ao dicionario
spell.word_frequency.load_words(['Douglas', 'Felippe', 'Stefanio', 'Amélia', 'Miguel', 'Arthur', 'Davi', 'Gabriel', 'Maria Eduarda', 'Alice', 'Heitor', 'Pedro', 'Laura', 'Douglas', 'Joaquim', 'Queiroz'])

#adiciona abreviacoes
spell.word_frequency.load_words(['mp', 'fb', 'jr', 'hd'])

abreviacoes = ["cv", "mp", "bpm", "av", "melissa", "sao", "melícia", "mto"]
significados = ["comando vermelho", "ministério público", "batalhão da polícia militar", "avenida", "milícia", "são", "milícia", "muito"]

repeticoes = ["aaa", "eee", "iii", "ooo", "uuu"] # lista para eliminacao de repeticoes de letras

for word in lista:
    if word in abreviacoes: # transforma a as abreviacoes da lista em seu significado
        word = significados[abreviacoes.index(word)]        
    
    for i in repeticoes: # procura por letras repetidas como na lista 'repeticoes' e elimina repeticao
        if i in word:
            lista[lista.index(word)] = ''.join(sorted(set(word), key=word.index))


#print (spell.known(misspelled))    # Returns those words that are in the word frequency list
#print (spell.unknown(misspelled))  # Returns those words that are not in the frequency list

for word in lista:
    f.write(spell.correction(word))
    f.write(" ") 