import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("Tesla is going to acquire twitter for $20 billion")

from spacy.tokens import Span
s1 = Span(doc,0,1,label='ORG')
s2 = Span(doc,5,6,label='ORG')
doc.set_ents([s1,s2],default='unmodified')

for ent in doc.ents:
    print(ent.text,'|',ent.label_)