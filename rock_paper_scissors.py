import random
def getUserchoice():
    userchoices = (input("enter chioces= "))
    return userchoices

# print(getUserchoice())

def getcomputerChoice():
    choices =(["rock","paper","scissors"])
    computerchioce = random.choice(choices)
    return computerchioce

print(getcomputerChoice())