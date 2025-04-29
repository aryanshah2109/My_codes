import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('Tony gave two $ to Peter')
token0 = doc[0]
print(token0)
print(token0.is_alpha)
print(token0.is_digit)

token2 = doc[2]
print(token2)
print(token2.is_digit)

token3 = doc[3]
print(token3)
print(token3.is_currency)


doc = nlp('Tony gave two $ to Peter, Bruce gave 500 € to Steve')
n = len(doc)
for i in range(n):
    if(doc[i].is_currency):
        print(doc[i-1],doc[i])