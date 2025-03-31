from nltk.corpus import stopwords
from nltk.tokenize import (sent_tokenize,word_tokenize)
corpus = '''The sun dipped below the horizon, painting the sky in shades of orange and purple. A cool breeze rustled the leaves as Emma sat on the porch, sipping her coffee. The distant hum of the city blended with the chirping of crickets, creating a peaceful symphony of the night. She took a deep breath, letting the crisp evening air fill her lungs. It had been a long day, but in this quiet moment, everything felt just right. The world slowed down, and for a little while, she simply existed—no worries, no deadlines, just the soft glow of the streetlights and the warmth of her cup. This is India
'''

sentences = sent_tokenize(corpus)
import nltk
for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    words = [word for word in words if word not in stopwords.words('english') ]
    posTag = nltk.pos_tag(words)
    print(posTag)

print("\n\n")
sent = "Taj Mahal is one of the 7 wonders"
words = word_tokenize(sent)
print(nltk.pos_tag(words))