import nltk

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

p_stemmer = PorterStemmer()

words = ['run', 'runner', 'running', 'ran', 'runs', 'easily', 'fairly']

for word in words:
    print(f'{word} ---> {p_stemmer.stem(word)}')

s_stemmer = SnowballStemmer(language='english')

words2 = ['generous', 'generation', 'generously', 'generate']

for word in words:
    print(f'{word} ---> {s_stemmer.stem(word)}')

phrase = 'I am meeting him tomorrow at the meeting'

for word in phrase.split():
    print(f'{word} ---> {p_stemmer.stem(word)}')
