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

`Doc.noun_chunks` are _base noun phrases_: token spans that include the noun and words describing the noun. Noun chunks
cannot be nested, cannot overlap, and do not involve prepositional phrases or relative clauses. Where `Doc.ents` rely on
the **_ner_** pipeline component, `Doc.noun_chunks` are provided by the parser.

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

### Viewing Matches
There are a few ways to fetch the text surrounding a match. The simplest is to grab a slice of tokens from the doc that
is wider than the match. Another way is to first apply the `sentencizer` to the Doc, then iterate through the sentence 
to the match point.

## Part of Speech Basics
Processing raw text intelligently is difficult, most words are rare, and it's common for words that look completely
different to mean almost the same thing. The same words in a different order can mean something completely different.
Even splitting text into useful word-like units can be difficult in many languages. While it's possible to solve some
problems starting from only the raw characters, it's usually better to use linguistic knowledge to add useful information.
That's exactly what spacy is designed to do, you put in raw text, and get back a `Doc` object, that comes with variety
of annotations. \

### POS Tags
In the English language, the same string of characters can have different meanings, even within the same sentence.
For this reason, morphology is important. spaCy uses machine learning algorithms to best predict the use of a token in 
a sentence.

### Counting POS Tags
The `Doc.count_by()` method accepts a specific token attribute as its argument, and returns a frequency count of the given
attribute as a dictionary object. Keys in the dictionary are the integer values of the given attribute ID, and values
are the frequency. Counts of zero are not included.

## Named Entity Recognition (NER)
spaCy has an `ner` pipeline component that identifies token spans fitting a predetermined set of named entities.
These are available as the `ents` property of a `Doc` object. \
Named-entity recognition (NER) seeks to locate and classify named entity mentions in unstrucutred text into pre-defined 
categories such as the person names, organizations, locations, medical codes, time expressions, quantities,
monetary values, percentages, etc.

`Doc.ents` are token spans with their own set of annotations:
* ent.text - The original entity text
* ent.label - The entity type's hash value
* ent.label_ - The entity type's string description
* ent.start - The token span's "start" index position in the Doc
* ent.end - The token span's "stop" index position in the Doc
* ent.start_char - The entity text's "start" index position in the Doc
* ent.end_char - The entity text's "stop" index position in the Doc

While spaCy may not have built-in tool for counting, we can pass a conditional statement into a list comprehension.

## Visualizing Named Entity Recognition
### Viewing Sentences Line by Line

Unlike the **displaCy** dependency parse, the NER viewer has to take in a Doc object with an `ents` attribute.
For this reason, we can't just pass a list of spans to `.render()`. We have to create a new Doc from each `span.text`.

## Sentence Segmentation
`Doc.sents` _**is a generator.**_ That is, a Doc is not segmented until `doc.sents` is called. This means that, where you 
could print the second Doc token with `print(doc[1])`, you can't call the "second Doc sentence" with `print(doc.sents[1])`.

### Adding Rules
spaCy's built-in `sentencizer` relies on the dependency parse and end-of-sentence punctuation to determine segmentation
rules. We can add rules of our own, but they have to be added before the creation of the Doc object, as that is where the 
parsing of segment start tokens happens. If we add a semicolon to our existing segmentation rules. This is, whenever the 
sentencizer encounters a semicolon, the next token should start a new segment.

### Changing the Rules
In some cases we want to _replace_ spacy's default sentencizer with our own set of rules. We have the capability to do that
so check the `sentence_segmentation.py` module.