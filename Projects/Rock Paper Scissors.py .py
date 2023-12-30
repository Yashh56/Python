# ROCK PAPER SCISSORS

import random


user_action=input("Enter a choice(Rock,Paper,Scissors):")


Possible_action=["Rock","Paper","Scissor"]

Comp_action=random.choice(Possible_action)

print(f"You Chose {user_action}, computer chose {Comp_action}")



if user_action == Comp_action:
    print(f"Both Player Selected {user_action}. It's Tie!!")

elif user_action == "Rock":
    if Comp_action=="Scissor":
        print("Rock Smashes Scissor! You Win!")
    else:
        print("Paper Covers The Rock! You Lose!")
elif user_action =="Paper":
    if Comp_action=="Scissor":
        print("Scissor Cuts The Paper! You Lose!")
    else:
        print("Paper Covers The Rock! You Win!")

        




