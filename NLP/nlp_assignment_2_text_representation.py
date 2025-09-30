# Problem 1
# Apply all the preprocessing techniques that you think are necessary

# Problem 2
# Find out the number of words in the entire corpus and also the total number of unique words(vocabulary) using just python

# Problem 3
# Apply One Hot Encoding

# Problem 4
# Apply bag words and find the vocabulary also find the times each word has occured

# Problem 5
# Apply bag of bi-gram and bag of tri-gram and write down your observation about the dimensionality of the vocabulary

# Problem 6
# Apply tf-idf and find out the idf scores of words, also find out the vocabulary.

import pandas as pd
import numpy as np
import emoji
import nltk
import spacy
import string
from textblob import TextBlob
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

data = pd.read_csv(r'D:\CODING_CODES\AIML\NLP\IMDB Dataset.csv')

df = data.sample(5)

print(df)
