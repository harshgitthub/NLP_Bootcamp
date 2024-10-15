import nltk
nltk.download('wordnet')
nltk.download('vader_lexicon')

from nltk.stem import PorterStemmer , WordNetLemmatizer 
text = """Welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demoWords = ["playing","happiness","going","doing","yes","no"," I","having","had","haved"]

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# this converts the words into there basic verb forms 
for word in demoWords:
    print(word , stemmer.stem(word),lemmatizer.lemmatize(word,"v"))

# sentiment analysis 

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("Programing is fun"))
print(sia.polarity_scores("Programing is bad"))