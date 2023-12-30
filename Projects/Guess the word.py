import random


name=input("What is your name ?")


print(f"Good Luck {name}!!")


words=["Ichigo","Luffy","Goku","Kakashi","Zoro","Urahara","Ayonkoji","Vegeta","Sauske","Renji","Shanks","Oden","Brook","Eren"]

word=random.choice(words)
print(word)

print("Guess the Characters")

guesses= ''

turns=12

while turns > 0:

    failed=0

    for char in word:
        
        if char in guesses:
            print(char,end=" ")

        else:
            print("_")

            failed+=1

    if failed==0:
        print("You Win!!")

        print("The Word is:",word)
        break
    print()
    guess=input("guess the character:")

    guesses+=guess

    if guess not in word:
        turns-=1

        print("Wrong")

        print("You have",+ turns,"more guesses")
        if turns==0:
            print("You Losse")



