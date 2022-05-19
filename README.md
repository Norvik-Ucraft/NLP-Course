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

## Stemming
Stemming is a somewhat crude method for cataloging related words, it essentially chops off letters from the end until the 
stem is reached. This works fairly well in most cases, but unfortunately English has many exceptions where a more 
sophisticated process is required. \
One of the most common and effective stemming tools is _**Porter's Algorithm**_. The algorithm employs five phases of
word reduction, each with its own set of mapping rules. \
_**Snowball**_ is the name of a stemming language, the algorithm used here is more acurately called the "English Stemmer"
or "Porter2 Stemmer". It offers a slight improvment over the original Porter stemmer, both logic and speed.

## Lemmatization
In contrast to stemming, lemmatization looks beyond word reduction, and considers a language's  full vocabulary to apply
a _morphological analysis_ to words. The lemma of 'was' is 'be' and the lemma of 'mice' is 'mouse'. Further, the lemma of 
'meeting' might be 'meet' or 'meeting' depending on its use in a sentence. Note that lemmatization does not reduce words 
to their most basic synonym. Although lemmatization looks at surrounding text to determine a given word's part of speech,
it does not categorize phrases.

## Stop Words
Words like 'a' and 'the' appear so frequently that they don't require tagging as thoroughly as nouns, verbs and modifiers.
We call these stop words, and they can be filtered from the text to be processed.

## Vocabulary and Matching
### Rule-based Matching
Spacy offers a rule-matching tool called `Matcher` that allows you to build a library of token patterns, then match those 
patterns against a Doc object to return a list of found matches. You can match on any part of the token including text and 
annotations, and you can add multiple patterns to the same matcher.
