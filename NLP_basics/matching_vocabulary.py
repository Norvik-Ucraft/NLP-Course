import spacy

from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

# here matcher is an object that pairs to the current Vocab object.
# we can add or remove specific named matchers to matcher as needed.
matcher = Matcher(nlp.vocab)

# looks for a single token whose lowercase text reads 'solarpower'
pattern1 = [{'LOWER': 'solarpower'}]

# looks for two adjacent tokens that read 'solar' and 'power' in that order
pattern2 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]

# looks for three adjacent tokens, with a middle token that can be any punctuation.
# single space are not tokenized, so they don't count as punctuation.
pattern3 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]

matcher.add('SolarPower', [pattern1, pattern2, pattern3])

doc = nlp('The Solar Power industry continues to grow as demand \
for solarpower increases. Solar-power cars are gaining popularity.')

found_matches = matcher(doc)

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)

# remove the old patterns to avoid duplication
matcher.remove('SolarPower')

# redefine the patterns
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '*'}, {'LOWER': 'power'}]
pattern3 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '*'}, {'LEMMA': 'power'}]

matcher.add('SolarPower', [pattern1, pattern2, pattern3])

doc2 = nlp('Solar-powered energy runs solar-powered cars.')

found_matches = matcher(doc2)

matcher2 = PhraseMatcher(nlp.vocab)

with open('../data/reaganomics.txt') as file:
    doc3 = nlp(file.read())

# create a list of match phrase
phrase_list = ['voodoo economics', 'supply-side economics', 'trickle-down economics', 'free-market economics']

# convert each phrase to a doc object
phrase_patterns = [nlp(text) for text in phrase_list]

# pass each doc object into matcher
matcher2.add('VoodooEconomics', [*phrase_patterns])

# build a list of matches
matches = matcher2(doc3)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc3[start:end]
    print(match_id, string_id, start, end, span.text)

# viewing matches
sents = [sent for sent in doc3.sents]

print(sents[0].start, sents[0].end)

for sent in sents:
    if matches[4][1] < sent.end:
        print(sent)
        break