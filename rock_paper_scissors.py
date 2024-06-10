import random
def getUserchoice():
    userchoices = (input("enter chioces= "))
    return userchoices

# print(getUserchoice())

def getcomputerChoice():
    choices =(["rock","paper","scissors"])
    computerchioce = random.choice(choices)
    return computerchioce

# print(getcomputerChoice())

def determinewinner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("tie")
    if user_choice == "rock":
        if computer_choice == "paper":
            print("computer wins")
    if user_choice == "paper":
        if computer_choice == "scissors":
            print("computer wins")
    if user_choice == "scissors":
        if computer_choice == "rock":
            print("computer wins")
    if user_choice == "paper":
        if computer_choice == "rock":
            print("user wins")
    if user_choice == "scissors":
        if computer_choice == "paper":
            print("user wins")
    if user_choice == "rock":
        if computer_choice == "scissors":
            print("user wins")
    
# user_choice = getUserchoice()
# computer_choice = getcomputerChoice()
# data=determinewinner(user_choice, computer_choice)
# print(data)


