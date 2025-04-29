print("Lemmatizing using spaCy: ")
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('eats eating ate eat adjustable remarking ability meeting better')
for token in doc:
    print(token.lemma_)

print("Lemmatizing using NLTK: ")
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
words = ['eats','eating','ate','eat','adjustable','remarking','ability','meeting','better']
for word in words:
    print(lemma.lemmatize(word))

print("Stemming using spaCy: ")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ['eats','eating','ate','eat','adjustable','remarking','ability','meeting','better']
for word in words:
    print(stemmer.stem(word))