__author__ = 'GAUTHAM HARI'
name = input("Hi, What is your name? ")
print("Hello " + name + "! Let's play a game!")
print("Think of a random number from 1 to 100, and try to guess it!")
count = 0
min = 0
max = 100
guess = 50
while(True):
    answer = input("Is it " + str(guess) + "? (yes/no) ")
    count += 1
    if(answer == "yes"):
        print("Yeey! I got it in " + str(count) + " tries!")
        play = input("Do you want to play more? (yes/no) ")
        if(play == "no"):
            print("Bye-bye")
            break
        else:
            count = 0
            min = 0
            max = 0
            guess = 50
            print("----------------------------------------------------------")
    else:
        clue = input("Is the number larger than " + str(guess) + "? (yes/no) ")
        if(clue == "yes"):
            min = guess
            difference = max-guess
            if(difference % 2 == 1):
                difference += 1
            guess += (difference)//2
        else:
            max = guess
            difference = guess - min
            if(difference % 2 == 1):
                difference -= 1
            guess -= (difference)//2

