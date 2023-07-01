"""
Write a progran to simulate the famous Rock-paper-scissors game 

Rules:
Rock wins Scissors 
Scissors wins paper
Paper wins Rock

Hint
1. There are two users: A human and computer
2. Use python random module to generate computer's play 
3. When users type in "q" or "quit", you should end the game 

Bonus.
keep track of the score
"""
from random import choice

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("choose an option from - rock, paper, scissors, q or quit:").lower()
    computer = choice(options)

    print("User choice: " + user)
    print("Computer choice: " + computer)

    if user == "q" or user == "quit":
        print("bye!!!")
        break
    elif user == computer:
        print("It's a tie")
    elif user == "rock" and computer == "paper":
        print("computer wins!")
        computer_score += 1
    elif user == "paper" and computer == "scissors":
        print("computer wins!")
        computer_score += 1
    elif user == "paper" and computer == "rock":
        print("you won!")
        user_score += 1
    elif user == "scissors" and computer == "rock":
        print("computer wins!")
        computer_score += 1
    elif user == "rock" and computer == "scissors":
        print("you won")
        user_score += 1
    elif user == "scissors" and computer == "paper":
        print("you won!")
        user_score += 1

print("User score: " + str(user_score))
print("Computer score: " + str(computer_score))


# ANOTHER WAY OF WRITING THE CODE

from random import choice

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    computer = choice(options)
    user = input("choose between(rock, paper, scisoors, q or quit) : ").lower()

    # output messages
    you_won = f"you: {user} \ncomputer: {computer} \nYou win!!!"
    you_lose = f"you: {user} \ncomputer: {computer} \nYou Lose!!!"
    tie = f"you: {user} \ncomputer: {computer} \nIt's a tie"
    score = f"computer: {computer_score}, you: {user_score}"

    if user in ["q", "quit"]:
        print("Bye !!!")
        break

    elif user not in options:
        print("INVALID!!!")

    else:
        if user == computer:
            print(tie)
            print(f"computer: {computer_score}, you: {user_score}")
        elif user == "rock" and computer == "scissors":
            user_score += 1
            print(you_won)
            print(f"computer: {computer_score}, you: {user_score}")
        elif user == "paper" and computer == "scissors":
            computer_score += 1
            print(you_lose)
            print(f"computer: {computer_score}, you: {user_score}")
        elif user == "scissors" and computer == "rock":
            computer_score += 1
            print(you_lose)
            print(f"computer: {computer_score}, you: {user_score}")
        elif user == "rock" and computer == "paper":
            computer_score += 1
            print(you_lose)
            print(f"computer: {computer_score}, you: {user_score}")
        elif user == "paper" and computer == "rock":
            user_score += 1
            print(you_won)
            print(f"computer: {computer_score}, you: {user_score}")
        elif user == "scissors" and computer == "paper":
            user_score += 1
            print(you_won)
            print(f"computer: {computer_score}, you: {user_score}")

print(score)
