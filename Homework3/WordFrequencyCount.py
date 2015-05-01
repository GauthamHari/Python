__author__ = 'GAUTHAM HARI'

def count_frequency(p):                     # Defining a function with one parameter
    d = {}                                  # Defining an empty dictionary
    p = sorted(p)                           # Sorting the list which was passed as input
    for word in p:                          # Looping through each word in the list
        d.update({word : p.count(word)})    # Adding a word and its count to the dictionary
        for word2 in p:                     # Looping through each word in the list
            if word2 == word:               # Checking for duplicate words
                p.remove(word2)             # Removing duplicate words from the list
    return d                                # Returning the dictionary

mylist = ["one","two","eleven","one","three","two","eleven","three","seven","eleven"]   # list with values
print(count_frequency(mylist))  # Calling the count frequency function by passing the list as input
