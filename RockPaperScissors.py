choices = ["rock","paper","scissors"]

import random



player = None
mac = random.choice(choices)

while player not in choices:
    player = input("rock, paper or scissors? ").lower()

if player == mac:
    print("mac: ",mac)
    print("player: ",player)
    print("Draw!")

elif player == "rock":
    if mac == "paper":
        print("mac: ",mac)
        print("player: ",player)
        print("You lose!")
    if mac == "scissors":
        print("mac: ",mac)
        print("player: ",player)
        print("You WIN!! TOO GOOD B)")
        
        
elif player == "paper":
    if mac == "scissors":
        print("mac: ",mac)
        print("player: ",player)
        print("You lose!")
    if mac == "rock":
        print("mac: ",mac)
        print("player: ",player)
        print("You WIN!! TOO GOOD B)")
        
elif player == "scissors":
    if mac == "rock":
        print("mac: ",mac)
        print("player: ",player)
        print("You lose!")
    if mac == "paper":
        print("mac: ",mac)
        print("player: ",player)
        print("You WIN!! TOO GOOD B)")
