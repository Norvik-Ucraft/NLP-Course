import spacy

from spacy.matcher import Matcher

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
