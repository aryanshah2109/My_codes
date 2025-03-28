# we pass the possible suffixes and prefixes we wish to remove.
# $ sign at the end means we only want to remove suffix
# without $ sign, all parts of the given word will be deleted
# min is used to give minimum length of the word to stem
# if length of word < min, it returns the same word without
# doing any stemming

from nltk.stem import RegexpStemmer
reg_stemmer = RegexpStemmer('ing$|able$|es|s$|ness',min=4)

print(reg_stemmer.stem('eating'))
print(reg_stemmer.stem('eats'))

# when no $, it removes the group of letters wherever found
# in the word
print(reg_stemmer.stem('nesshappyness'))

# when length of word < min, it returns original word without 
# stemming
print(reg_stemmer.stem('aes'))