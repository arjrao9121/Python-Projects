# Author - arjrao9
# purpose of this code is to check the password strenght of the user.

import getpass

condition = True
score = 0
lowerCase = False
upperCase = False
specialChars = False
numberChars = False


def inputProcessor():

    global score 

    while condition:

        password = getpass.getpass('What is your password?')

        if (len(password) < 8 or len(password) > 16):

            print(
                "The password you have entered is not BETWEEN 8-16 characters long! ❌❌"
            )

            print("This was your password: ", password)

            retry = input('Do you wish to try again? y/n: ')

            if retry == 'y':
                continue
            else:
                break
        else:
            passwordProcessor(password)

            print("Your password was: ", password)

            resultProcessor(lowerCase, upperCase, numberChars, specialChars)

            toUseagain = input("Do you want to try again? y/n: ")

            score = 0

            if toUseagain == 'y':
                continue
            else:
                break


def passwordProcessor(passW):
    global upperCase, lowerCase, numberChars, specialChars
    for character in passW:
        if character in "abcdefghijklmnopqrstuvwxyz":
            lowerCase = True
        elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upperCase = True
        elif character in "0123456789":
            numberChars = True
        elif character in "!@#$%^&*":
            specialChars = True


def resultProcessor(lowerCase, upperCase, number, specialChars):
    global score
    if lowerCase == True:
        print("Your password must include a lowercase character [a-z]: ✅ ")
        updateScore()
    else:
        print("Your password must include a lowercase character [a-z]: ❌ ")

    if upperCase == True:
        print("Your password must include an Uppercase character [A-Z]: ✅ ")
        updateScore()
    else:
        print("Your password must include a lowercase character [A-Z]: ❌ ")

    if number == True:
        print("Your password must include a number [0-9]: ✅ ")
        updateScore()
    else:
        print("Your password must include a number [0-9]: ❌ ")

    if specialChars == True:
        print("Your password must include a special character [!@#$%^&*]: ✅ ")
        updateScore()
    else:
        print("Your password must include a special character [!@#$%^&*]: ❌ ")

    print("Your Current Score is: ",score)


def updateScore():
    global score
    score = score + 25

def main():
    inputProcessor()


if __name__ == '__main__':
    main()
