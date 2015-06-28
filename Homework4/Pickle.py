__author__ = 'GAUTHAM HARI'

import pickle

def unpickle_data():
    input_file = open("pickles.txt","br")
    return_list = pickle.load(input_file)    #unpickling
    print("Data_Pickled:\n", return_list)
    input_file.close()

output_file = open("pickles.txt","bw")
print("PICKLING PROGRAM")
name = input("Enter your Name: ")
age = input("Enter your Age: ")
country = input("Enter your Country of Origin: ")
mylist = [name, age, country]
pickle.dump(mylist, output_file)     #pickling
output_file.close()

unpickle_data()     #calling unpickling function
