# 
# Implementation of Sentiment analysis
# Adapted from
# https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386

import sys
import os
import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

class s1_analysis(object):
    def __init__(self, modeldir="./"):
        self.classifier = None
        self.training_set = None
        self.testing_set = None
        self.word_features = None
        self.traindir = modeldir + "/train"
        self.testdir = modeldir + "/test"
        return

    # Function to create a dictionary of features for each review in the list
    # document. The keys are the words in word_features
    # The values of each key are either true or false for whether that feature
    # appears in the review or not.
    def find_features(self, document):
        words = word_tokenize(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)
        return features

    def build_feature_sets(self):
        files_pos = os.listdir(self.traindir + "/pos")
        files_pos = [open((self.traindir + "/pos/") +f, 'r').read() for f in files_pos]
        files_neg = os.listdir(self.traindir + "/neg")
        files_neg = [open((self.traindir + "/neg/") +f, 'r').read() for f in files_neg]

        all_words = []
        documents = []
        stop_words = list(set(stopwords.words("english")))

        #  j is adject, r is adverb, and v is verb
        #allowed_word_types = ["J","R","V"]
        allowed_word_types = ["J"]

        for p in  files_pos:
            # create a list of tuples where the first element of each tuple is a review
            # the second element is the label
            documents.append( (p, "pos") )

            # remove punctuations
            cleaned = re.sub(r'[^(a-zA-Z)\s]','', p)

            # tokenize
            tokenized = word_tokenize(cleaned)

            # remove stopwords
            stopped = [w for w in tokenized if not w in stop_words]

            # parts of speech tagging for each word
            pos = nltk.pos_tag(stopped)

            # make a list of  all adjectives identified by the allowed word types list above
            for w in pos:
                if w[1][0] in allowed_word_types:
                    all_words.append(w[0].lower())


        for p in files_neg:
            # create a list of tuples where the first element of each tuple is a review
            # the second element is the label
            documents.append( (p, "neg") )

            # remove punctuations
            cleaned = re.sub(r'[^(a-zA-Z)\s]','', p)

            # tokenize
            tokenized = word_tokenize(cleaned)

            # remove stopwords
            stopped = [w for w in tokenized if not w in stop_words]

            # parts of speech tagging for each word
            neg = nltk.pos_tag(stopped)

            # make a list of  all adjectives identified by the allowed word types list above
            for w in neg:
                if w[1][0] in allowed_word_types:
                    all_words.append(w[0].lower())

        # creating a frequency distribution of each adjectives.
        all_words = nltk.FreqDist(all_words)

        # listing the 5000 most frequent words
        self.word_features = list(all_words.keys())[:5000]

        # Creating features for each review
        featuresets = [(self.find_features(rev), category) for
                       (rev, category) in documents]

        # Shuffling the documents
        random.shuffle(featuresets)

        self.training_set = featuresets[:20000]
        self.testing_set = featuresets[20000:]
        return

    def train(self):
        self.build_feature_sets()
        self.classifier = nltk.NaiveBayesClassifier.train(self.training_set)
        print("Classifier accuracy percent:",
                (nltk.classify.accuracy(self.classifier, self.testing_set))*100)
        self.classifier.show_most_informative_features(15)
        return

    def train_save(self, model_filename):
        pickle.dump(self.classifier, open(model_filename, "wb"))
        pickle.dump(self.word_features, open(model_filename + "word_features", "wb"))
        return

    def train_load(self, model_filename):
        self.classifier = pickle.load(open(model_filename, "rb"))
        self.word_features = pickle.load(open(model_filename + "word_features", "rb"))
        return

if __name__ == "__main__":
    pass
