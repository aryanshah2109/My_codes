import spacy
nlp = spacy.load('en_core_web_sm')

print(nlp.pipe_names)

# you can add lemma for your custom words like slangs using 
# attribute ruler

ar = nlp.get_pipe('attribute_ruler')
ar.add(
    [[{'TEXT':"Bro"}],[{'TEXT':'Bruh'}]],
    {'LEMMA':'Brother'}
)

doc = nlp('Bro! I just earned $5 from Naman Bruh')
for word in doc:
    print(word.lemma_)

# without adding the custom lemma we were getting bro for bro
# and bruh for bruh but after adding custom lemma we are getting
# brother for bro and bruh