__author__ = 'GAUTHAM HARI'

import os

direct = '.'
file_name = input("Please enter the name of the file you need to scan: ")
for dirName, subdirList, fileList in os.walk(direct):
    print('Found directory: %s' % dirName)
    for fname in fileList :
        if file_name == fname:
            f = open(os.path.join(dirName,file_name))
            print('\t%s' % file_name)
            print("path is :",f)
            content = f.read()
            if 'password=' in content:
                print("WARNING: This file contains insecure text!")
            f.close()
