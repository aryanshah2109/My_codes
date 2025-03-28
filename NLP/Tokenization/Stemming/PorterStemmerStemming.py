# stemming is a nlp technique to reduce words into their roots by removing suffixes
# and prefixes 
# some words might be incorrectly stemmed which means that their root might not be 
# of the same meaning as the original. this is a disadvantage of stemming

from nltk.stem import PorterStemmer
words = ['eating','eaten','eats','programs','programming','fairly','sportingly','programmer','historical']
stemming = PorterStemmer()
for word in words:
    print(word,"--->",stemming.stem(word))

# improper stemming congratulations -> congratul which has no meaning
print(stemming.stem('congratulations'))