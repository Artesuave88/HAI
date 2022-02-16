# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:17:34 2021

@author: admin
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import string    
import nltk
flag=True

#Extract data, tokenize it  and take care of casing
f = open('SQuAD_Beyonce.csv', 'r', encoding='utf-8')
raw_content = f.read().lower()
sent_tokens = nltk.sent_tokenize(raw_content)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw_content)# converts to list of words
stop_words = set(stopwords.words('english'))  
#Checks if each word in the word tokens is a stop word. If not, adds it to filtered document.  
filtered_doc = []

for word in word_tokens:  
    if word not in stop_words:  
        filtered_doc.append(word)
#Vocabulary is the filtered document.
vocabulary=filtered_doc

#lemmers the tokens
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#lemmers the stop words to match the preprocessing
def _lem(self, token):
    if (token in stop_words):
            return token 
    return self.lemmer.lem(token)

#Function to get best answer to question
def response(user_response):
    response=''
#takes user input
    sent_tokens.append(user_response)
#Convert a collection of raw documents to a matrix of TF-IDF features
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    
#the responses comes from here.
    idx=vals.argsort()[0][-2]
    
#flattens and sorts the vector into linear.
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

#if theres no good similarity
    if(req_tfidf==0):
        response=response+"I am sorry! I don't understand you"
        return response
#if there is a similarity
    else:
        response = response+ sent_tokens[idx]
        return response
    
print("TROC: What would you like to know about Beyonce?")
print("TROC: I'm her biggest fan!")
while(flag==True): 



    user_response = input()
    user_response=user_response.lower().translate(remove_punct_dict)        

            #user wants to end chat        
    if(user_response=='bye'):
                       
                        print("TROC: Bye! take care..")
                        flag=False
    if(user_response=='no'):

                        print("TROC: Bye! take care..")
                        flag=False
    else:                   
                    print("TROC: "+response(user_response))
                    sent_tokens.remove(user_response)
                    print("TROC: Anything else?")



#END of IRBOT
