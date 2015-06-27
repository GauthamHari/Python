__author__ = 'GAUTHAM HARI'
class Animal:

    def __init__(self, name):
        self.name = name        #instance variable

    def guess_who_am_i(self):   #instance method
        guess = ""
        print("\nI will give you 3 hints, guess what animal I am")

        if(self.name == "elephant"):    #Checking for elephant
            print("\nI have exceptional memory")    #Hint 1
            guess = input("Who am I?: ")
            if(guess.lower() == "elephant"):
                print("You got it! I am elephant")
                return
            else:
                print("Nope, try again!")
                print("\nI am the largest land-living mammal in the world")     #Hint 2
                guess = input("Who am I?: ")
                if(guess.lower() == "elephant"):
                    print("You got it! I am elephant")
                    return
                else:
                    print("Nope, try again!")
                    print("\nI have a Tusk")    #Hint 3
                    guess = input("Who am I?: ")
                    if(guess.lower() == "elephant"):
                        print("You got it! I am elephant")
                        return
                    else:
                        print("Nope, try again!")
                        print("\nI'm out of hints! The answer is: elephant")
                        return

        elif(self.name == "tiger"):     #Checking for tiger
            print("\nI am the biggest cat")     #Hint 1
            guess = input("Who am I?: ")
            if(guess.lower() == "tiger"):
                print("You got it! I am tiger")
                return
            else:
                print("Nope, try again!")
                print("\nI come in black and white or orange and black")    #Hint 2
                guess = input("Who am I?: ")
                if(guess.lower() == "tiger"):
                    print("You got it! I am tiger")
                    return
                else:
                    print("Nope, try again!")
                    print("\nI am the national animal of Bangladesh, India, Vietnam, Malaysia and South Korea")    #Hint 3
                    guess = input("Who am I?: ")
                    if(guess.lower() == "tiger"):
                        print("You got it! I am tiger")
                        return
                    else:
                        print("Nope, try again!")
                        print("\nI'm out of hints! The answer is: tiger")
                        return

        elif(self.name == "bat"):   #Checking for bat
            print("\nI use echo-location")  #Hint 1
            guess = input("Who am I?: ")
            if(guess.lower() == "bat"):
                print("You got it! I am bat")
                return
            else:
                print("Nope, try again!")
                print("\nI can fly")    #Hint 2
                guess = input("Who am I?: ")
                if(guess.lower() == "bat"):
                    print("You got it! I am bat")
                    return
                else:
                    print("Nope, try again!")
                    print("\nI see well in dark")   #Hint 3
                    guess = input("Who am I?: ")
                    if(guess.lower() == "bat"):
                        print("You got it! I am bat")
                        return
                    else:
                        print("Nope, try again!")
                        print("\nI'm out of hints! The answer is: bat")
                        return

e = Animal("elephant")  #class object creation
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()      #calling instance method
t.guess_who_am_i()
b.guess_who_am_i()