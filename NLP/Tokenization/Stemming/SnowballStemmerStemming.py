# better alternative as compared to PorterStemmer
# gives better roots than it
from nltk.stem import SnowballStemmer

words = ['eating','eaten','eats','programs','programming','fairly','sportingly','programmer','historical']

snowball_stem = SnowballStemmer('english')
for word in words:
    print(word+'---->'+snowball_stem.stem(word))

