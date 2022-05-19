import spacy

nlp = spacy.load('en_core_web_sm')


def show_lemmas(doc):
    for token in doc:
        print(f'{token.text:{12}}\t{token.pos_:{6}}\t{token.lemma:<{22}}\t{token.lemma_}')


doc = nlp('I am a runner in a race because I love to run since I ran today')
doc2 = nlp('I saw eighteen mice today!')
doc3 = nlp('I am meeting him tomorrow at the meeting.')
doc4 = nlp('That\'s an enourmous automobile')

show_lemmas(doc4)
