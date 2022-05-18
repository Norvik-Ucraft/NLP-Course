import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp('Tesla is looking at buying U.S. startup for $6 million')

# tokenize
# for token in doc:
#     print(token.text, token.pos_, token.dep_)

# nlp pipeline
pipeline = nlp.pipeline

# name of the pipes
pipes_name = nlp.pipe_names

doc2 = nlp('Tesla is not looking into startup anymore')

# for token in doc2:
#     print(token.text, token.pos_, token.dep_)

doc3 = nlp('Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
the phrase "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

life_quote = doc3[16:30]

# print(type(life_quote))

# Sentence tokenizer
doc4 = nlp('This is the first sentence. This is another sentence. This is the last sentence.')

# for sentence in doc4.sents:
#     print(sentence)

sentence_start = doc4[6].is_sent_start
