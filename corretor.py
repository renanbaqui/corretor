from spellchecker import SpellChecker

with open('teste2.txt') as f:
    lista=[word for line in f for word in line.split()]

#print(lista)

unknown = flat_list
spell = SpellChecker(language='pt')

# find those words that may be misspelled
misspelled = spell.unknown(lista)


print (spell.known(misspelled)) # Returns those words that are in the word frequency list
print (spell.unknown(misspelled)) # Returns those words that are not in the frequency list

for word in misspelled:
    # Get the one `most likely` answer
    print('palavra errada:')
    print(word)
    print(spell.correction(word))

    # Get a list of `likely` options
    #print(spell.candidates(word))

    #print(spell.word_usage_frequency(word)) # The frequency of the given word out of all words in the frequency list