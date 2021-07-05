import re


def inputProcessor():

    condition = True

    while condition:

        password = input("Please enter your password: ")

        if (len(password) < 8 or len(password) > 16):
            print("Your password must be between 8-16 characters long")
            break

        elif not re.search('[a-z]', password):
            print("Password must countain letters from [a-z]")

            break

        elif not re.search('[0-9]', password):
            print("Password must countain at least one letter from [0-9]")
            print("Password strenght = 50/100")
            break

        elif not re.search('[A-Z]', password):
            print(
                "Password must countain at least one capital letter from [A-Z]"
            )

            print("Password strenght = 75/100")

            break

        elif not re.search('[!@#$%^*]', password):
            print(
                "Password must countain at least one special character [!@#$%^&*]"
            )

            print("Password strenght = 80/100")

            break

        print("Good Job you have a good pass word!")
        print("Password strenght = 100/100")

        tryAgain = input('Do you wish to try again? y/n: ')

        if tryAgain == "y":
            continue
        else:
            break


def main():

    inputProcessor()


if __name__ == '__main__':
    main()
