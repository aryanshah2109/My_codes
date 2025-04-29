import spacy
nlp = spacy.load("en_core_web_sm")


doc = nlp("A newer version of spaCy is now available.")
token = doc[4]
print(token)
group = list(token.subtree)
print(" ".join([t.text for t in group]))
      