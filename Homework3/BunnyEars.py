__author__ = 'GAUTHAM HARI'

def bunny_ears(p):                      # Recursive function
    if(p < 1):                          # Checking if number of bunnies is zero or negative
        return 0                        # Returning zero
    elif p % 2 == 0:                    # Checking for even number
        return bunny_ears(p-1) + 3      # Even bunnies have 3 ears
    else:                               # Checking for odd number
        return bunny_ears(p-1) + 2      # Odd bunnies have 2 ears

print("bunnyEars(0) -> " + str(bunny_ears(0)))  # Function call with 0 bunny
print("bunnyEars(1) -> " + str(bunny_ears(1)))  # Function call with 1 bunny
print("bunnyEars(2) -> " + str(bunny_ears(2)))  # Function call with 2 bunnies
