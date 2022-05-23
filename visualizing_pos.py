import spacy

from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp('The quick brown fox jumped over the lazy dog\'s back.')

# render the dependency parse immediately inside Jupyter:
displacy.render(doc, style='dep', jupyter=True, options={'distance': 110})

for token in doc:
    print(f'{token.text:{10}} {token.pos_:{7}} {token.dep_:{7}} {spacy.explain(token.dep_)}')

displacy.serve(doc, style='dep', options={'distance': 110})

# Since large text are difficult to view on one line. you will pass a list of spans instead.
# Each span will apear on its own line.

doc2 = nlp('This is a sentece. This is another, possibly longer sentece.')

# create spans from Doc.sents
spans = list(doc2.sents)

displacy.serve(spans, style='dep', options={'distance': 110})

# customizing the Appearance
options = {'distance': 110, 'compact': 'True', 'color': 'yellow', 'bg': '#09a3d5', 'font': 'Times'}

displacy.serve(spans, style='dep', options=options)
