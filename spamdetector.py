'''
NLP Stages
Lexical Processing
Syntactic Processing
Semantic Processing

Basic Lexical Processing:
	word Frequency and Stopwords {nltk}----FreqDist()
	Tokenization {nltk.tokenize}-----word_tokenize(), regexp_tokenize()
	Bag-of-words [Vectorizer] {sklearn.feature_extraction.text}----- CountVectorizer()
	Stemming {nltk.stem}-------PorterStemmer(), SnowballStemmer() 
	Lemmatization{ntlk.stem}-------WordNetLemmatizer()
	Tf-idf {sklearn.feature_extraction.text}------TfidfVectorizer()
	Canoniicalisation--Phonetic Hashing---------Soundex Algorithm
	Edit Distance{ntlk.metrices.distance}/Levenshtein Edit Distance Alorithm | Damerau-Levenshtein Distance
	Pointwise Mutual Information----Probability
 '''
import random
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
## Reading the given dataset
spam = pd.read_csv("SMSSpamCollection.txt", sep = "\t", names=["label", "message"])
data_set = []
for index,row in spam.iterrows():
    data_set.append((row['message'], row['label']))
stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
def preprocess(document, stem=True):
    'changes document to lower case, removes stopwords and lemmatizes/stems the remainder of the sentence'

    # change sentence to lower case
    document = document.lower()

    # tokenize into words
    words = word_tokenize(document)

    # remove stop words
    words = [word for word in words if word not in stopwords.words("english")]

    if stem:
        words = [stemmer.stem(word) for word in words]
    else:
        words = [wordnet_lemmatizer.lemmatize(word, pos='v') for word in words]

    # join words to make sentence
    document = " ".join(words)

    return document
messages_set = []
for (message, label) in data_set:
    words_filtered = [e.lower() for e in preprocess(message, stem=False).split() if len(e) >= 3]
    messages_set.append((words_filtered, label))
def get_words_in_messages(messages):
    all_words = []
    for (message, label) in messages:
      all_words.extend(message)
    return all_words

def get_word_features(wordlist):

    #print(wordlist[:10])
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
word_features = get_word_features(get_words_in_messages(messages_set))
sliceIndex = int((len(messages_set)*.8))
random.shuffle(messages_set)
train_messages, test_messages = messages_set[:sliceIndex], messages_set[sliceIndex:]

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, train_messages)
testing_set = nltk.classify.apply_features(extract_features, test_messages)

spamClassifier = nltk.NaiveBayesClassifier.train(training_set)

#print(nltk.classify.accuracy(spamClassifier, training_set))
#print(nltk.classify.accuracy(spamClassifier, testing_set))

m = 'CONGRATULATIONS!! As a valued account holder you have been selected to receive a £900 prize reward! Valid 12 hours only.'
print('Classification result : ', spamClassifier.classify(extract_features(m.split())))

print(spamClassifier.show_most_informative_features(50))

## storing the classifier on disk for later usage
import pickle
f = open('nb_spam_classifier.pickle', 'wb')
pickle.dump(spamClassifier,f)
print('Classifier stored at ', f.name)
f.close()
