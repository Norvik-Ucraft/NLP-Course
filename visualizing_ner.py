import spacy

from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp('Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million. '
          'By contrast, Sony sold only 7 thousand Walkman music players.')

displacy.render(doc, style='ent', jupyter=True)

for sent in doc.sents:
    displacy.render(nlp(sent.text), style='ent', jupyter=True)

doc2 = nlp('Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.'
           'By contrast, my kids sold a lot of lemonade.')

for sent in doc2.sents:
    displacy.render(nlp(sent.text), style='ent', jupyter=True)

for sent in doc2.sents:
    docx = nlp(sent.text)
    if docx.ents:
        displacy.render(docx, style='ent', jupyter=True)
    else:
        print(docx.text)

# you can pass a list of entity to restrict the visualization
options = {'ents': ['ORG', 'PRODUCT']}

displacy.render(doc, style='ent', jupyter=True, options=options)

# you can also pass background color and gradient options
colors = {'ORG': 'linear-gradient(90deg, #aa9cfc, #fc9ce7)', 'PRODUCT': 'radial-gradient(yellow, green)'}
options = {'ents': ['ORG', 'PRODUCT'], 'colors': colors}

displacy.render(doc, style='ent', jupyter=True, options=options)

# creating visualizations outside Jupyter
displacy.serve(doc, style='ent', options=options)