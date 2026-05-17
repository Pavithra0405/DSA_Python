print('Hi this is my first python program')

# input and output
print('Hello,What is ur name?')
name = input()
print('Hi,',name)

# operators
print('Enter num1')
num1 = int(input())
print('Enter num2')
num2 = int(input())
print('Enter num3')
num3 = int(input())
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num3 / num2)
print(num1 ** num2)
print(num1 % num2)
print(num3 // num2)
print(type(num1))
print(type(num2))
print(type(num3))

# conditions
print(2 < 5)
print(2 > 5)
print(2 == 5)
print(2 != 5)
print('Hello' == 'hello')
print('hi' == '5')

# IF/ELIF/ELSE
height = int(input('enter your height:'))
if height <= 1:
    print('You are 1m!!!')
elif height > 5:
    print('you are tall')
else:
    print('Invalid input')

# chained conditionals and nested statements
x = 2
y = 3
# and
print("AND")
if x == y and x + y == 5: #false /true
    print("true")
else:
    print('false')
# or
print("OR")
if x == y or x + y == 5: # false / True
    print("true")
else:
    print('false')
print("NOT")
if not(x == y): # !false => true
    print("true")
else:
    print('false')