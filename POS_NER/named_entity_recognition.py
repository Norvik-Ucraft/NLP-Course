import spacy

from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(f'{ent.text} - {ent.label_} - {spacy.explain(ent.label_)}')
    else:
        print('No named entities found.')


doc = nlp('May I go to Washington, DC next May to see the Washington Monument?')

show_ents(doc)

doc2 = nlp('Can I please borrow 500 dollars from you to buy some Microsoft stock?')

for ent in doc2.ents:
    print(ent.text, ent.start, ent.end, ent.start_char, ent.end_char, ent.label_)

doc3 = nlp('Tesla to build a U.K. factory for $6 million')

show_ents(doc3)

ORG = doc.vocab.strings['ORG']

new_ent = Span(doc3, 0, 1, label=ORG)

doc3.ents = list(doc3.ents) + [new_ent]

show_ents(doc3)

doc4 = nlp('Our company plans to introduce a new vacuum cleaner.'
           'If successful, the vacuum-cleaner will be our first product.')

show_ents(doc4)

# Apply the patterns to our matcher object
phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]

# Apply the patterns to our matcher object
matcher = PhraseMatcher(nlp.vocab)
matcher.add('newproduct', [*phrase_patterns])

# Apply the matcher to our Doc object
matches = matcher(doc4)

PROD = doc.vocab.strings['PRODUCT']

new_ent2 = [Span(doc4, match[1], match[2], label=PROD) for match in matches]

doc4.ents = list(doc4.ents) + new_ent2

show_ents(doc4)

doc5 = nlp('Originally priced a $29.50, the sweater was marked down to five dollars.')

show_ents(doc5)

count_ent = len([ent for ent in doc5.ents if ent.label_ == 'MONEY'])

doc6 = nlp('Autonomous cars shift insurance liability toward manufacturers.')

for chunk in doc6.noun_chunks:
    print(f'{chunk.text} - {chunk.root.text} - {chunk.root.dep_} - {chunk.root.head.text}')

noun_chunk_count = len(list(doc6.noun_chunks))

print(noun_chunk_count)
