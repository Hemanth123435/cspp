import random
def getUserChoice():
    choice = input("enter choice= ")
    return choice
# print(getUserChoice())

def getcomputerChoice():
    choices =(["rock","paper","scissors"])
    computerchioce = random.choice(choices)
    return computerchioce

print(getcomputerChoice())