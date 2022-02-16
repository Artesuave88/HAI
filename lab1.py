# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:03:42 2021

@author: admin
"""

import nltk

from nltk import word_tokenize
from urllib import request
url = "http://www.gutenberg.org/files/84/84-0.txt" 
content = request.urlopen(url).read().decode('utf8', errors='ignore')

print(len(content)) # print the length of the text

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet') # This specific line only needs to be run once
lemmatiser = WordNetLemmatizer()

p_stemmer = PorterStemmer()
sb_stemmer = SnowballStemmer('english')
sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."
print(sentence)
for token in word_tokenize(sentence):
    print("Stemming:")
    print(p_stemmer.stem(token))
    print("Lemming:")
    print(lemmatiser.lemmatize(token))
    print("---")
