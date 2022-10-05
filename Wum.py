import colorama
from colorama import *
import requests
import random

c = Fore.CYAN 

ai_name = "Wum"
ai = "Wum:"

greet = ["hi", "Hi", "hello", "Hello", "hey", "Hey"]
ai_feel = ["good","awesome","incredible","fine","great"]

again = 0
num = ["0","1","2","3","4","5","6","7","8","9"]

s_bot = True
while s_bot == True:
    
    command = str(input("> "))

    if "bored" in command or "am doing nothing" in command:
        r = requests.get('http://www.boredapi.com/api/activity/').json()
        act = r['activity']
        print(ai, act)
        print("")
        


    if "how are you" in command or "How are you" in command:
        random.shuffle(ai_feel)
        if again == 0:
            print(ai, "I am feeling", ai_feel[0] + "!")
            print("")
            again += 1
        elif again == 1:
            print(ai, "I already told you that I am feeling", ai_feel[0] + "!!!")
            print("")
            again += 1
        elif again == 2:
            print(ai, "Do you even listen to me..")
            print("")
            again = 0
         


    #if command in greet:
    if "hi" in command or "Hi" in command or  "hello" in command or "Hello" in command or  "hey" in command or  "Hey" in command:
        print(ai, "Hello! What can I help you with ?")
        print("")

    if "fact" in command:
        r = requests.get('https://asli-fun-fact-api.herokuapp.com/').json()
        activity = r['data']['fact']
        print(ai, activity)
        print("")

    r = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist').json()
    if "joke" in command:
        print(ai, "You want a joke? Here you go!")
        print("")
        if r.get('setup') == None:
            
        
            first_part = r['joke']
            print(ai, first_part)
            print("")

        else:
            
            first_part = r['setup']
            s = r['delivery']
            print(ai, first_part)
            print(ai, s)
            print("")
            