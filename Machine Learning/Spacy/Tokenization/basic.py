import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Hey! My name is Aryan Shah. I am studying NLP while in my 4th semester. I pay $1600 as a fee in my college.")

for sentences in doc.sents:
    for words in sentences:
        print(words)

