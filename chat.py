# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:05:48 2021

@author: admin
"""
import nltk
import random
#Hard coded small talk. Dumb AI!!!
greetings= ("hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "g’day", "howdy")
thanks=("You’re welcome.","No problem.","No worries.","Don’t mention it.","My pleasure.","Anytime.","It was the least I could do.","Glad to help.","Sure!","Thank you.")
how=("How are you?","How you?", "how are you doing?")

#creates negative words dataset
#Extract data, tokenize it  and take care of casing
f = open('negative.csv', 'r', encoding='utf-8')
raw_neg= f.read().lower()
word_neg = nltk.word_tokenize(raw_neg)# converts to list of words

#creates positive words dataset
#Extract data, tokenize it  and take care of casing
f = open('positive.csv', 'r', encoding='utf-8')
raw_pos= f.read().lower()
word_pos = nltk.word_tokenize(raw_pos)# converts to list of words

#creates small talk dataset
#Extract data, tokenize it  and take care of casing
f = open('smalltalk.csv', 'r', encoding='utf-8')
raw_small= f.read().lower()
sent_small = nltk.sent_tokenize(raw_small)# converts to list of sentences 

print("TROC: Lets Chat")
print("TROC: type bye to leave")
print("TROC: "+random.choice(how))
user_response = input()
user_response=user_response.lower()  

if(user_response in raw_pos):
        print("TROC: awesome!")
        while(user_response!='bye'):
            print("TROC: "+random.choice(sent_small))
            user_response = input()
            user_response=user_response.lower()  
        if(user_response== 'bye'):
            print("TROC: hmmmm, I see!")
            print("TROC: I need to go now. Bye! take care..")   
            flag=False          
        
if(user_response in raw_neg):
        print("TROC: Ahh too bad!")
        while(user_response!='bye'):
            print("TROC: "+random.choice(sent_small))
            user_response = input()
            user_response=user_response.lower()  
        if(user_response== 'bye'):
            print("TROC: hmmmm, I see!")
            print("TROC: I need to go now. Bye! take care..")   
            flag=False      
        
if("how are you" in user_response):
        print("TROC: "+random.choice(raw_pos))
        user_response = input()
        user_response=user_response.lower()   
        if(user_response=='bye'):
            print("TROC: Bye! take care..")   
            flag=False
    #small talk 
if(user_response in greetings):
        print("TROC: "+random.choice(greetings))
        user_response = input()
        user_response=user_response.lower()
        #user wants to end chat        
        if(user_response=='bye'):
            print("TROC: Bye! take care..")   
            flag=False
