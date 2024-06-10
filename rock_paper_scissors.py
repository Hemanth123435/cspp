import random
def getUserChoice():
    choice = input("enter choice= ")
    return choice
# print(getUserChoice())

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
    
# user_choice = getUserChoice()
# computer_choice = getcomputerChoice()
# data=determinewinner(user_choice, computer_choice)
# print(data)

def play():
    print("welcome to rockpaperscissors game")
    print("rock")
    print("paper")
    print("scissors")
    # n=(input("enter chioces"))
    user_choice = getUserChoice()
    computer_choice = getcomputerChoice()
    data=determinewinner(user_choice, computer_choice)
    return(data)


play()