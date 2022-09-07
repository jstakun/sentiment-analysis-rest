import re
import string

import nltk
from sklearn.base import BaseEstimator, TransformerMixin


class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        self.patterns = ["<.+?>", "\S*\d+\S*"]
        self.stopwords = nltk.corpus.stopwords.words('english') + ["'ll", "'re", "'m"]
        self.punk_table = str.maketrans({key: None for key in string.punctuation})
        self.stemmer = nltk.PorterStemmer()

    def fit(self, X, y=None):
        return self # unused method

    def transform(self, X):
        for pattern in self.patterns:
            X = [re.sub(pattern, '', rev) for rev in X]
        X = [rev.lower() for rev in X]
        X = [nltk.word_tokenize(rev) for rev in X]
        X = [[token for token in rev if token not in self.stopwords] for rev in X]
        X = [[self.stemmer.stem(token) for token in rev] for rev in X]
        X = [" ".join(rev) for rev in X]
        X = [rev.translate(self.punk_table) for rev in X]
        return X
