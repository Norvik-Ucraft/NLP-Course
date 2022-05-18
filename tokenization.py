import spacy

nlp = spacy.load('en_core_web_sm')

mystring = '"We\'re moving to L.A.!"'
doc = nlp(mystring)

for token in doc:
    print(token.text, end=' | ')

doc2 = nlp("We're here to help! Send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")

for token in doc2:
    print(token.text)

doc3 = nlp('A 5km NYC cab ride costs $10.30')

for token in doc3:
    print(token.text)

doc4 = nlp('Let\'s visit St. Louis in the U.S. next year.')

for token in doc4:
    print(token.text)

# Vocab objects contains a full library of items
vocab_len = len(doc4.vocab)

print(vocab_len)

doc5 = nlp('Apple to build a Hong Kong factory for $6 million')

for token in doc5:
    print(token.text, end=' | ')

for ent in doc5.ents:
    print(ent.text)
    print(ent.label_)
    print(str(spacy.explain(ent.label_)))
    print('\n')