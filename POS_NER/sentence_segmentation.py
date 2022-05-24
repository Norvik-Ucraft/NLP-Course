import spacy

from spacy.language import Language
from seg.newline.segmenter import NewLineSegmenter

nlp = spacy.load('en_core_web_sm')

doc = nlp('This is the first sentence. This is another sentence. This is the last sentence.')

for sent in doc.sents:
    print(sent)

doc_sents = [sent for sent in doc.sents]

print(doc_sents)
print(type(doc_sents[1]))
print(doc_sents[1].start, doc_sents[1].end)

# Parsing the segmentation start tokens happens during the nlp pipeline
doc2 = nlp('This is a sentence. This is a sentence. This is a sentence.')

for token in doc2:
    print(f'{token.is_sent_start}   {token.text}')

doc3 = nlp('"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc3.sents:
    print(sent)


# Add new rule to pipeline
@Language.component('component')
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc


nlp.add_pipe('component', before='parser')

pipe_names = nlp.pipe_names

doc4 = nlp('"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc4.sents:
    print(sent)

nlp = spacy.load('en_core_web_sm')

mystring = 'This is a sentence. This is another.\n\nThis is a \nthird sentence.'

# spacy default behavior
doc5 = nlp(mystring)

for sent in doc.sents:
    print([token.text for token in sent])
