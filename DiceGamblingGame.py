import random

dchoices = ["1", "2", "3", "4", "5","6"]


again = True 


while again:

    player = None
    mac = random.choice(dchoices)

    multiplier = int("3")

    bet = int(input('How much money do you want to bet? '))
    number = input('what is guess? (From a Number 1-6) ')

    bruh = (bet)*multiplier

    if number == mac:
        print("Player's number = ", number)
        print("The Computer's Number = ", mac)
        print("Congrats You won! $", multiplier*int(bet))
    
        anotherroll = input('Do you wish to play again? (y/n) ')

        if anotherroll == "y":
            continue
        else:
            break

    if number != mac:
        print("player's number = ", number)
        print("The Computer's Number = ", mac)
        print("You Lost all your money LOL B)")

        anotherroll = input('Do you wish to play again? (y/n) ')

        if anotherroll == "y":
            continue
        else:
            break


