import spacy
nlp = spacy.load('en_core_web_lg')

doc = nlp("dog cat tree banana apple afnjcar")

for token in doc:
    print(token,"Vector: ",token.has_vector,",","Out of vocab: ",token.is_oov)

# printing the vector of dog
print(doc[0].vector)
print(doc[0].vector.shape)
