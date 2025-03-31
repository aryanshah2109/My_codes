# lemmetization is like stemming except it returns root word 
# instead of root stem. 
# output is called lemma
# it is more accurate than stemming
# we use lemmatization in Q/A, chatbots, text summarization
# lemmatization is slower than stemming

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# POS tags:
# 'n' - noun
# 'v' - verb
# 'a' - adjective
# 'r' - adverb
# by default pos tag is noun

print(lemmatizer.lemmatize('going'))
print(lemmatizer.lemmatize('going',pos='v'))

print(lemmatizer.lemmatize('congratulations'))

