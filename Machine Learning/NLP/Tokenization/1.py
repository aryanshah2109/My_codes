from nltk.tokenize import sent_tokenize

corpus = """Hello. I am Aryan Shah.
Welcome to my AIML package!
Today we will learn about tokenization.
We will use nltk library of python.
"""

print(sent_tokenize(corpus))

documents = sent_tokenize(corpus)

from nltk.tokenize import word_tokenize
print(word_tokenize(corpus))

for sentences in documents:
    print(word_tokenize(sentences))
