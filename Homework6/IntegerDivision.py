__author__ = 'GAUTHAM HARI'

from random import randrange

print("INTEGER DIVISIONS")
while(True):
    a = randrange(5)    #Selecting a random number between 0 and 4
    b = randrange(5)

    try:
        result = a//b                                       #Floor division. May throw ZeroDivisionError
        guess = int(input(str(a) + "/" + str(b) + "="))     #User input may throw ValueError
    except ZeroDivisionError:                               #Handling ZeroDivisionError
        continue
    except ValueError:                                      #Handling bad input entered by the user
        print("Please enter Integers only!")
        continue
    else:
        if(str(result) == str(guess)):                      #Checking if user entered the correct answer
            print("CORRECT!")                               #Providing feedback to the user
        else:
            print("INCORRECT!")
