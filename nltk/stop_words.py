import nltk 
nltk.download('stopwords')


text = """Welcome you to programming knowledge. Let's start with our first tutorial on NLTK."""
demoWords = ["playing","happiness","going","doing","yes","no" ,"I"]

from nltk.corpus import stopwords 
stop_words = set(stopwords.words("english"))
print(stop_words)

from nltk.tokenize import word_tokenize , sent_tokenize
tokenize_words = word_tokenize(text)
print(tokenize_words)

tokenize_words_without_stop_words = []
for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)

print("stop words which got removed",set(tokenize_words) - set(tokenize_words_without_stop_words))
print(tokenize_words)
print(tokenize_words_without_stop_words)