from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
sentence = "Apple Inc. is planning to open a new store in Paris on October 15, 2024 at 10:00am. Tim Cook, the CEO, will attend the opening ceremony."

words = word_tokenize(sentence)
newWords = [word for word in words if word not in stopwords.words('english')]


posTag = nltk.pos_tag(words)
ner = nltk.ne_chunk(posTag).draw()
# print(ner)