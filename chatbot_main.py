import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
flag=True

    
#Intent matching openening options
print("TROC: Welcome to the Totaly Random Options Chatbot")
print("TROC: People call me TROC")
print("TROC: What is your name?")

name=input()

print("TROC: It's good to meet you " + name + "! If you want to exit, type Bye!")
print("TROC: Select what you'd like to do (1,2,3):")
print("TROC: 1: Ask me a question about Beyonce")
print("TROC: 2: Play a game")
print("TROC: 3: Have a chat")
print("TROC: 4: Leave")

user_response=input()
#name handling
if("what" and "my name" in user_response):
                print("TROC: " + name +" . Is that correct?")
                user_response = input()
                user_response=user_response.lower()                
                if("no" in user_response):
                    print("TROC: What would you like to change your name to?")
                    name=input()
                    print("TROC: Ok "+name+". How can i help?")
                    print("TROC: 1: Ask me a question (About Beyonce)")
                    print("TROC: 2: Play a game")
                    print("TROC: 3: Have a chat")
                    print("TROC: 4: Leave")
                    user_response = input()
                    user_response=user_response.lower()   
                
               
                else:
                    print("TROC: Ok "+name+". How can i help?")
                    print("TROC: 1: Ask me a question (About Beyonce)")
                    print("TROC: 2: Play a game")
                    print("TROC: 3: Have a chat")
                    print("TROC: 4: Leave")

                    user_response = input()
                    user_response=user_response.lower()   

#name changing            
if("change" and "name?" in user_response):
                print("TROC: What would you like to change your name to?")
                name=input()
                print("TROC: Ok "+name+". How can i help?")
                print("TROC: 1: Ask me a question (About Beyonce)")
                print("TROC: 2: Play a game")
                print("TROC: 3: Have a chat")
                print("TROC: 4: Leave")

                user_response = input()
                user_response=user_response.lower()   

     

    
if(user_response=='bye'):
        print("TROC: Bye! take care..")   
        flag=False
        
#runs game file
if(user_response=='2'):
    exec(open("game.py").read())

    
#runs chat file
if(user_response=="3"):
    exec(open("chat.py").read())

#runs question answer file
if(user_response=="1"):

   exec(open("QA.py").read())

if(user_response=="4"):
    flag=False  
else:
    print("TROC: Please select an option (1,2,3)")
    print("TROC: 1: Ask me a question (About Beyonce)") 
    print("TROC: 2: Play a game")
    print("TROC: 3: Have a chat")
    print("TROC: 4: Leave")
    user_response = input()
    user_response=user_response.lower()    
#runs game file
if(user_response=='2'):
    exec(open("game.py").read())

    
#runs chat file
if(user_response=="3"):
    exec(open("chat.py").read())

#runs question answer file
if(user_response=="1"):

   exec(open("QA.py").read())    
if(user_response=="4"):
    flag=False    

else:
    print("TROC: Please select an option (1,2,3)")
    print("TROC: 1: Ask me a question (About Beyonce)") 
    print("TROC: 2: Play a game")
    print("TROC: 3: Have a chat")
    print("TROC: 4: Leave")
    user_response = input()
    user_response=user_response.lower()    
#runs game file
if(user_response=='2'):
    exec(open("game.py").read())

    
#runs chat file
if(user_response=="3"):
    exec(open("chat.py").read())

#runs question answer file
if(user_response=="1"):

   exec(open("QA.py").read())    
if(user_response=="4"):
    flag=False    
    
else:
    print("TROC: Please select an option (1,2,3)")
    print("TROC: 1: Ask me a question (About Beyonce)") 
    print("TROC: 2: Play a game")
    print("TROC: 3: Have a chat")
    print("TROC: 4: Leave")
    user_response = input()
    user_response=user_response.lower()    
#runs game file
if(user_response=='2'):
    exec(open("game.py").read())

    
#runs chat file
if(user_response=="3"):
    exec(open("chat.py").read())

#runs question answer file
if(user_response=="1"):

   exec(open("QA.py").read())    
if(user_response=="4"):
    flag=False    