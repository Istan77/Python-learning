def add(x, y):
    z=x+y
    return z

def sub(x,y):
    return x-y

def mult(x,y):
    z=x*y
    return z

def Hello():
    z = "goodbye"
    return z

def math(x):
    z=x(2,3)
    return z

#list_A = [0,1,2,3,4,5,6]
list_A = [1,1,1,1,1,1,1]
list_B = range(10)

list_C = range(4,48,11)

def Funk_list_add(x,y):
    for i in range(len(x)):
        print(x[i]+y[i])

#x = input("Type a number and press enter...\n\t")
#while(True):
#    print("hello")
        
#x = int(input("List 8 reasons why the civil war was important below.\n\t 1.\n\t 2.\n\t 3.\n\t 4.\n\t 5.\n\t 6.\n\t 7.\n\t 8.\n\t"))

'''
if (x <5):
    print("less than 5")
    
print("this")
#else:
#    print("greater than 5 or equal to")


print(x) #not casting the char
print( int(y) ) #casting the char to an int
'''

print("Welcome to Dan's calculator!\n\n")

while True:
    x = input("\n\nInput the first number...\n")
    y = input("Input the second number...\n")

    x = int(x)
    y = int(y)
        
    while True:
        c = input("select the number of the operation you would like to perform\n\t 1 = Add\n\t2 =Subtract\n\t3 = Multiply\n")
        c = int(c)
        
        if c == 1:
            print("The answer is "+str(add(x,y)))
            break
        elif c == 2:
            print("The answer is "+str(sub(x,y)))
            break
        elif c == 3:
            print("The answer is "+str(mult(x,y)))
            break
        else:
            print("ya fucked up!")

    e = int(input("would you like to stop?\n\t1 = Yes\n\t2 = No"))

    if e == 1:
        print("\nGoodbye!\n")
        break          
