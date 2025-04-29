import spacy
nlp = spacy.load("en_core_web_sm")
text = '''When updating to a newer version of spaCy, it's generally recommended to start with a clean virtual environment. If you're upgrading to a new major version, make sure you have the latest compatible trained pipelines installed, and that there are no old and incompatible packages left over in your environment, as this can often lead to unexpected results and errors. If you've trained your own models, keep in mind that your train and runtime inputs must match. This means you'll have to retrain your pipelines with the new version.
'''
doc = nlp(text)
print(doc)

print(len(text))
print(len(doc))

# doc -> considers tokens instead of letters
# tokens may include words and puntatutions
# however text considers individual characters
# hence len(text) > len(doc)

for sent in doc.sents:
    print(sent)

sentence1 = list(doc.sents)[0]
print(sentence1)

token = sentence1[7]
print(token)

print(token.text)
print(token.left_edge)