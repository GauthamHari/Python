__author__ = 'GAUTHAM HARI'

import shelve
from datetime import datetime, date

#Dictionary
my_dictionary = {'Name':'Gautham Hari',
                 'City':'West Haven',
                 'Apt.no':'2',
                 'Street Name':'Treat Street',
                 'Zipcode':'06516'}

start_time = datetime.now().time()
print("Starting time:", start_time)

print('06516' in my_dictionary.values())
for info in my_dictionary:
    print("The data contained is {0} : {1}.".format(info, my_dictionary[info]))

end_time = datetime.now().time()
print("End time:", end_time)
print("")

#--------------------------------------------------------------------------------------------------

#Shelving
print("{0}{1}{2}.".format(10*'-','Execution time for Shelve',10*'-'))
my_shelve = shelve.open("my_shelve")
my_shelve['data'] = {'Name':'Gautham Hari',
                 'City':'West Haven',
                 'Apt.no':'2',
                 'Street Name':'Treat Street',
                 'Zipcode':'06516'}

start_time_shelve = datetime.now().time()
print("Starting time:", start_time_shelve)

print('data' in my_shelve)
for info in my_shelve:
    print("The data contained is {0} : {1}.".format(info,my_shelve[info]))

end_time_shelve = datetime.now().time()
print("End time:", end_time_shelve)