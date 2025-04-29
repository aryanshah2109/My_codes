'''
1) Extract all NOUN tokens from this story. You will have to read the file in python first to collect all the text and then extract NOUNs in a python list
2) Extract all numbers (NUM POS type) in a python list
3) Print a count of all POS tags in this story
'''

import spacy
import spacy.attrs
nlp = spacy.load('en_core_web_sm')

with open(r'D:\CODING_CODES\AIML\Machine Learning\Spacy\POS\news_story.txt','r') as f:
    text = f.read()

doc = nlp(text)
list_nouns = []
list_pos_num = []
for token in doc:
    if token.pos_  in ['NOUN']:
        list_nouns.append(token)
    list_pos_num.append(token.pos)

print(list_nouns)
print(list_pos_num)
count = doc.count_by(spacy.attrs.POS)
print(count)

