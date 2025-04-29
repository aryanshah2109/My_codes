import spacy
import spacy.attrs
nlp = spacy.load('en_core_web_sm')
doc = nlp('Elon wants to buy Twitter for a lot of money!')
for token in doc:
    print(token,' | ',token.pos_)


# find out number of POS used in the corpus
count = doc.count_by(spacy.attrs.POS)
print(count)