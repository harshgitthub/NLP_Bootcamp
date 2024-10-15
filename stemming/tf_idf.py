import nltk 
from nltk.text import TextCollection

mytexts = TextCollection(['the universe has very many stars','the galaxy contains many stars'])



print(mytexts._texts)
print(mytexts.tf_idf('universe','the universe has very many stars'))