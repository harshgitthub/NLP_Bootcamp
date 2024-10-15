import nltk 
import matplotlib.pyplot as plt 


# Download 'punkt' tokenizer specifically, instead of opening the full downloader GUI
# import nltk
# nltk.download()


text = """Welcome you to programming knowledge. Let's start with our first tutorial on NLTK."""

# Tokenize words
from nltk import word_tokenize
#print("Word Tokenization:", word_tokenize(text))

# Tokenize sentences
from nltk import sent_tokenize
#print("Sentence Tokenization:", sent_tokenize(text))

word_tokenized = word_tokenize(text)

from nltk.probability import FreqDist
fd = FreqDist(word_tokenized)
print(fd.most_common(3))
fd.plot(30, cumulative=False)
plt.show()