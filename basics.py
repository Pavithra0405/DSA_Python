# loops
# For loop
for x in range(0,10,1):
    print(x)
    
# while loop
loop = True
while loop:
    name = input("Enter something: ")
    if name == 'stop':
        loop = False
        break