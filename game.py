# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:57:41 2021

@author: admin
"""
import time
flag=True


print("TROC: Lets Play a Game ")
print("Welcome to the Adventure Game!\n\n")
print("You are the legendary adventurer Axel Stone!")
print("With no food and no weapons, you must find your way to shelter")
health = 100
print("Are your ready?")
ready=input()
if ready=="no":
        print("\nExiting...")
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1
        print()
        flag==False
        
else:
        print("Please wait!")
        time.sleep(1)
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1

        print("\nYour current health is ", health)
        print("Let's play!\n")

        time.sleep(2)

        left_or_right = input("First choice... In front of you stands 2 roads. Which do you take? Left or Right (left/right)? ")
        if left_or_right == "left":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            ans = input(
                "\nNice, you follow the road and find a sword on the floor.\nIn front of you is a Goblin. Do you attack the goblin? (yes/no)")

            if ans == "yes":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou swing at the Goblin, amongst the battle he wounds you. However, you kill him.")
                print("You lose 25 health.")
                health -= 25
                print("health= ",health)
                ans = input(
                "\nYou notice a house and a river. Which do you go to (river/house)? ")
                
                if ans == "house":
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1
                    print("\nYou go to the house and are greeted by the owner... He doesn't like you and hits you with a stick.")
                    print("You lose 15 health.")
                    health -= 15
                    print("Health= ",health)
                    print("Do you strike him with your sword?(yes/no)")
                    ans=input()
                    if ans=="yes":
                        count = 0
                        while count != 5:
                            print(".", end="")
                            time.sleep(2/5)
                            count += 1
                        print("\nWell done, he was the evil wizard Zork. You are now safe!!")
                    if ans=="no":
                        print("\nThe man was the evil wizard Zork. He casts a spell on you and turns you to ash.\nYou are dead!")
                        flag=False
                if ans=="river":
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1

                    print("\nYou fell in the river and die...")
                    print("You're dead!")
                    flag = False



            if ans == "no":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nThe Goblin decides to attack you first. As your swords is not raised, he strikes you dead.")
                print("You are dead!")
                flag=False
                


               
        if left_or_right == "right":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1
            print("\nThe road is blocked by a gang of Orcs. Each one thirsty for your flesh. They rip you apart.")
            print("You're dead!")
            flag = False
