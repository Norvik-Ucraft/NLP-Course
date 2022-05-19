import spacy

nlp = spacy.load('en_core_web_sm')

print(nlp.Defaults.stop_words)

# check if the word is a stop word
word = nlp.vocab['myself'].is_stop
word2 = nlp.vocab['mystery'].is_stop

# add custom word to set of spacy stop wrords.
nlp.Defaults.stop_words.add('btw')

# set the stop_word tag on the lexeme
nlp.vocab['btw'].is_stop = True

word3 = nlp.vocab['btw'].is_stop

print(nlp.Defaults.stop_words)

# remove a word from set of spacy stop words
nlp.Defaults.stop_words.remove('beyond')

# remove the stop_word tag from lexeme
nlp.vocab['beyond'].is_stop = False

word4 = nlp.vocab['beyond'].is_stop
