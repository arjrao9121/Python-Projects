num1 = int(input('What is the first number?'))

print(num1)


num2 = int(input('What is your second number?'))

print(num2)

output = input('What operation would you like to perform? (+, -, *, /)')

if output == '+':
    print(num1 + num2)
    
if output == '-':
    print(num1 - num2)
    
if output == '*':
    print(num1*num2)
    
if output == '/':
    print(num1/num2)
