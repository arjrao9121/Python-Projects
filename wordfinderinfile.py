import os, re


def inputProcessor():

    folderLocation = input("Please provide the Location of folder? ")

    # change the location of the folder to the specified location provided by the user.
    os.chdir(folderLocation)

    print("Path has been changed to " + folderLocation)

    fileName = input("Please provide file Name? ")

    fileProcessor(fileName)


def fileProcessor(fileName):
    

    cond = True

    while cond:

        # read the file
        file = open(fileName, 'r')

        word = input(
            "Please provide the word you are looking for. (Please type exit() to exit) "
        )

        searchListCounter = 0

        if word != 'exit()':
            pattern = '(?:' + word + ')'

            for line in file:
                search = re.findall(pattern, line)
                searchListCounter = searchListCounter + search.count(word)

            print("Total number of " + word + " found: " + str(searchListCounter))
            continue


        else:
            cond = False


def main():
    inputProcessor()


if __name__ == "__main__":
    main()
