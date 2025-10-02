# START ON LINE 38


import os
import time

print("hint: type in the number that matches your choice, and press enter!\n")

for i in range(5):
    time.sleep(1)
    print(".")


time.sleep(2)
os.system("clear")

#####################
def fixInput(userInput, goodInputList):
    while userInput not in goodInputList:
        userInput = input("> ")
    return userInput
######

# GIFT #
def gift():
    print("gift option")
############

# PARTY #
def party():
    print("party option")
############

# FRIEND #
def f_bdayBestieCall():
    print("""What should you say?
    (1) Hi! Can you like plan a bday party for our friend? lol thanks ig
    (2) omg gurl you suck, what are you doing??? plan a party for our friend
    (3) Hey girl!! I was wondering if you had any plans this weekend? Maybe we could surprise our friend with a birthday party?""")
    ##### START HERE!!!!!!!!########

def friend():
    print("friend option")
    print("Wow, okay, rude.")
    time.sleep(1)
    print("At least come up with something yourself?")
    time.sleep(1)
    print("Oh well, I guess you'll text someone...")
    time.sleep(1)
    print("""Who should you ask?
    (1) The birthday person's best friend
    (2) The birthday person's worst enemy
    (3) Your best friend
    (4) The class gossip
    (5) The birthday person's parents
    """)
    f_Call = input("> ")
    f_Call = fixInput(f_Call, ["1", "2", "3", "4", "5"])
    print("your input was !!fixed!!")
    if f_Call == "1": #bday's bestie
        f_bdayBestieCall()

    elif f_Call == "2": #bday's enemy
        2
    elif f_Call == "3": #your bestie
        3
    elif f_Call == "4": #snitch/gossip
        4
    elif f_Call == "5": #bday's parents
        5

############

######################

print("It's your friend's birthday!\n\n")


print("""What are you going to do?
    (1) Buy them a gift
    (2) Plan a surprise party
    (3) Make someone else plan a surprise party
    """)

pathChoice = input("> ")

pathChoice = fixInput(pathChoice, ["1", "2", "3"])
if pathChoice == "1":
    gift()
elif pathChoice == "2":
    party()
elif pathChoice == "3":
    friend()

#####################

print("yay!")
