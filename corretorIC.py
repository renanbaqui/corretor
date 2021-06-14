from spellchecker import SpellChecker
from nltk.tokenize import RegexpTokenizer

with open('relatos.txt', 'r', encoding='utf-8') as text_file:   #abre o arquivo com encoding utf-8
    str = text_file.read()  #transforma o texto em string

f = open("erros.txt", "w")

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

tokenizer = RegexpTokenizer(r'\w+')     #tokenizer do nlkt
lista = tokenizer.tokenize(str2)        #string tokenizado em lista

#print(lista)    #imprime a lista de tokens para debug

#unknown = flat_list
spell = SpellChecker(language='pt')     #cria objeto do tipo SpellChecker em portugues


#adiciona nomes próprios ao dicionario
spell.word_frequency.load_words(['Felippe', 'Stefanio', 'Amélia', 'Miguel', 'Arthur', 'Davi', 'Gabriel', 'Maria Eduarda', 'Alice', 'Heitor', 'Pedro', 'Laura'])

#adiciona abreviacoes
spell.word_frequency.load_words(['mp', 'fb', 'jr', 'hd'])


# find those words that may be misspelled
misspelled = spell.unknown(lista)   #utiliza o metodo unknown do objeto spell para criar uma lista de palavras erradas 'misspelled'


#print (spell.known(misspelled))    # Returns those words that are in the word frequency list
#print (spell.unknown(misspelled))  # Returns those words that are not in the frequency list


for word in lista:
    f.write(spell.correction(word))
    f.write(" ")