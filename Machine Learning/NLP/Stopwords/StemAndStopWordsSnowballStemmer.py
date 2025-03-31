from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

corpus = '''The sun dipped below the horizon, painting the sky in shades of orange and purple. A cool breeze rustled the leaves as Emma sat on the porch, sipping her coffee. The distant hum of the city blended with the chirping of crickets, creating a peaceful symphony of the night. She took a deep breath, letting the crisp evening air fill her lungs. It had been a long day, but in this quiet moment, everything felt just right. The world slowed down, and for a little while, she simply existed—no worries, no deadlines, just the soft glow of the streetlights and the warmth of her cup.
'''

snowballStemmer = SnowballStemmer('english')
sentences = sent_tokenize(corpus)

for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    words = [snowballStemmer.stem(word) for word in words if word not in stopwords.words('english')]
    sentences[i] = ' '.join(words)
print(sentences)

