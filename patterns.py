name = "Ahmed"
print(name) #Ahmed

newName = None
# Ahme, Ahm, Ah, A
newName_pattern_two = ""

for i in range(len(name)):
    
    if newName != None:
        newString = newName.rstrip(newName[-1])
        
        if newString != "":
            newName = newString
            print(newName)
        
    else:
        newString = name.rstrip(name[-1])
        newName = newString
        print(newName)
newName = None 
        
for i in (name):
    newName_pattern_two += i 
    print(newName_pattern_two)
