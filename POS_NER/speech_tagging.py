import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp('The quick brown fox jumped over the lazy dog\'s back.')


def pos(doc):
    print(doc.text, '\n')
    for token in doc:
        print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')


pos(doc)

doc2 = nlp('I\'m reading books on NLP.')

token = doc2[2]

print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')

doc3 = nlp('I read a book on NLP.')

token2 = doc3[1]

print(f'{token2.text:{10}} {token2.pos_:{8}} {token2.tag_:{6}} {spacy.explain(token2.tag_)}')

doc4 = nlp('The quick brown fox jumped over the lazy dog\'s back.')

# count the frequencies of different coarse-grained POS tags
POS_counts = doc.count_by(spacy.attrs.POS)

print(POS_counts)

decoded_attribute = doc.vocab[92].text

print(decoded_attribute)

for k, v in sorted(POS_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{5}}: {v}')

# count the different fine-grained tags
TAG_counts = doc.count_by(spacy.attrs.TAG)

for k, v in sorted(TAG_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')

# Count of different syntactic dependencies
DEP_counts = doc.count_by(spacy.attrs.DEP)

for k, v in sorted(DEP_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')