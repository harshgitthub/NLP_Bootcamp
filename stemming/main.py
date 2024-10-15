"""
refers to the process of reducing the inflected words to their word stem or base-form 
generally a written word form .
grouping words with same meaning together .

"""

import nltk 
from nltk.stem import PorterStemmer

porter = PorterStemmer()

word_list= ["argue","argued","argues","arguing","argues"]

for word in word_list:
    # this gives the stem of all these words [argu : slub ]
    print(porter.stem(word))

print("\n")
# the root and stem words are different here argue :  root word while , argu is the stem 

from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language="english")
lancaster = LancasterStemmer()

for word in word_list:
    # this gives the stem of all these words [argu : slub ]
    print(snowball.stem(word))

print("\n")
for word in word_list:
    # this gives the stem of all these words [argu : slub ]
    print(lancaster.stem(word))