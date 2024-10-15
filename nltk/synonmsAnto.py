import nltk 

from nltk.corpus import wordnet 

syn = wordnet.synsets("computer")
print(syn[0].definition()) # definition 

synonyms =[]

for syt in wordnet.synsets('computer'):
    for lemma in syt.lemmas():
        synonyms.append(lemma.name())

print(synonyms)


antonyms =[]

for syt in wordnet.synsets('computer'):
    for lemma in syt.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
        

print(antonyms)