from spellchecker import SpellChecker
from nltk.tokenize import RegexpTokenizer

with open('relatos.txt', 'r', encoding='utf-8') as text_file:   #abre o arquivo com encoding utf-8
    str = text_file.read()  #transforma o texto em string

f = open("erros.txt", "w")

#print(str)

tokenizer = RegexpTokenizer(r'\w+')     #tokenizer do nlkt
lista = tokenizer.tokenize(str)         #string tokenizado em lista

#print(lista)

#unknown = flat_list
spell = SpellChecker(language='pt')     #objeto do tipo SpellChecker em portugues

# find those words that may be misspelled
misspelled = spell.unknown(lista)       #lista de palavras erradas 


#print (spell.known(misspelled))    # Returns those words that are in the word frequency list
#print (spell.unknown(misspelled))  # Returns those words that are not in the frequency list

for word in misspelled:
    # Get the one `most likely` answer
    f.write("palavra errada encontrada:")
    f.write("\n")
    f.write(word)
    f.write("\n")    
    f.write("sugestao de palavra correta:")
    f.write("\n")
    f.write(spell.correction(word))
    f.write("\n")
    
    print('palavra errada encontrada:')
    print(word)
    print('sugestao de palavra correta:')
    print(spell.correction(word))

    # Get a list of `likely` options
    #print(spell.candidates(word))

    #print(spell.word_usage_frequency(word)) # The frequency of the given word out of all words in the frequency list