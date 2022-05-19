# NLP-Course

## What is Spacy?
Spacy is open source Natural Language Processing Library, designed to effectively handle NLP tasks with the most efficient
implementation of common algorithms. For many NLP tasks, Spacy only has one implemented method, choosing the most efficient 
algorithms currently available, this means we often don't have the option to choose other algorithms.

Spacy works with a Pipeline object and the main idea here is that there is an `nlp()` function from spacy automatically 
takes raw text and performs a series of operations to tag, parse, and describe the text data.

Spacy will isolate punctuation that does not form an integral part of a word. Quotation marks, commas, and punctuation
at the end of a sentence will be assigned their own token. However, punctuation that exists as part of an email address,
website or numerical value will be kept as part of the token.

## What is NLTK?
NLTK - Natural Language Toolkit is a very popular open source. It provides many functionalities, but includes less
efficient implementations.

## What is NLP?
Natural Language Processing (NLP) is an area of computer science and artificial intelligence concerned with the interactions
between computers and humans (natural) languages, in particular how to program computers to process and analyze large 
amounts of natural language data. \
Natural Language Processing attempts to use a variety of techniques in order to create structure out of text data.

## Tokenization
The first step in processing text is to split up all the component parts (words & punctuation) into "tokens". These tokens
are annotated inside the Doc object to contain descriptive information. \
Tokens are the basic building blocks of a Doc object - everything that helps us understand the meaning of the text is
derived from tokens and their relationship to one another. \
`Doc` objects can be thought of as list of `token` objects. As such, individual tokens can be retrieved by index position,
and spans of tokens can be retrieved through slicing. \
Although `Doc` objects can be considered lists of tokens, _they do not support item reassignment_.

## Named Entities
Named Entities add another layer of context. The language model recognize that certain words are organizational names while
others are locations, and still other combinations relate to money, dates, etc. Named entities are accessible through
the `ents` property of a `Doc` object.

## Noun Chunks
Similar to `Doc.ents`, `Doc.noun_chunks` are another object property. Noun chunks are "_base noun phrase_" - flat phrases
that have a noun as their head. You can think of noun chunks as a noun plus the words describing the noun.

## Built-in Visualizers
Spacy includes a built-in visualization tool called _**displaCy**_. displacy is able to detect whether you're working in 
a Jupyter notebook, and will return markup that can be rendered in a cell right away. When you export your notebook, the 
visualizations will be included as HTML.