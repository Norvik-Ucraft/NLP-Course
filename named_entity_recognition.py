import spacy

from spacy.tokens import Span

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
