__author__ = 'GAUTHAM HARI'

import os

print("FILE FINDER PROGRAM")
print("The existing directories are listed below")
print(os.listdir('C:\\'))

file_path = ""
search_path = input("Please enter the directory you want to search for: ")
file_name = input("Please enter the file name you want to search for: ")

if os.path.isdir(search_path):
    for paths in search_path:
        file_path = os.path.join(search_path, file_name)
        if os.path.isfile(file_path):
            print("Your file is found in " + file_path)
            break
    else:
        print("No such file in the directory")
else:
    print("No such directory")
