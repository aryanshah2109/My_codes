import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load('en_core_web_sm')
doc = nlp('We just opened our wings, the flying part is coming soon')

# list up all non stop words
non_stop = [token.text for token in doc if not token.is_stop and not token.is_punct]
print(non_stop)


