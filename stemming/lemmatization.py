import nltk 
from nltk.stem import WordNetLemmatizer

"""
the difference from the stemmer is that stemmer operates on words without the knowledege of the context therefore
it cannot differentiate between words which have different meaning depending on part of sentence 
"""

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("bats"))
# by default part of speech is noun unless specified 

# stop words : commonly used word but they don't carry any meaning 
# case folding : converting all to lower / upper cases 
# topic modelling : finding topics in a given corpus 