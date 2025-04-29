import spacy
nlp = spacy.load('en_core_web_lg')

doc = nlp('dog cat apple banana tree flag ape')

doc2 = nlp("mango")

# printing the similarities between two words
for token in doc:
    print(f"{token.text}<->{doc2[0].text} = {token.similarity(doc2[0])}")
