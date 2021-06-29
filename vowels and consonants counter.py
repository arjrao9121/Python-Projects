



from io import StringIO


inputFileName = input("Enter name of input file: ")
inputFile = open(inputFileName, "r")


count = 0

c = 0


vowels = ["a", "e", "i", "o", "u"]

consonents = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# print(inputFile.read()) -- prints the whole file B)

vowelsdata = {}.fromkeys(vowels, 0)

consonentsdata = {}.fromkeys(consonents, 0)


string = inputFile.read()

String = string.lower()

for char in String:
    if char in vowels:
        count = count+1 

print("Total num of vowels are: ", count)



for char in String:
    if char in vowels:
        vowelsdata[char] += 1


print(vowelsdata)

for char in String:
    if char in consonents:
        c = c+1

print("The total number of Consonents are ", c)


for char in String:
    if char in consonents:
        consonentsdata[char] += 1

print(consonentsdata)






    








