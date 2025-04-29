import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('Tesla is going to buy Twitter INC. for $45 billion')
for ent in doc.ents:
    print(ent.text,'|',ent.label_)

print(doc.ents)