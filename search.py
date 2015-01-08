#!/usr/bin/env python

''' Provides a facility for the searching of the filesystem '''

import os

def md5(string):
    import hashlib
    return hashlib.md5(string).hexdigest()

def query_filesystem(string):
    startcwd = os.getcwd()
    for index, character in enumerate(string):
        if os.path.isdir(string[index]):
            os.chdir(string[index])
        else:
            return
    if startcwd != os.getcwd():
        return os.getcwd() + '/plaintext.txt'
    else:
        return

def read_plaintext(path):
    fd = open(path, 'r')
    data = fd.readline()
    fd.close()
    return data

def search(string):
    result = query_filesystem(string)
    if result:
        return read_plaintext(result)
    else:
        return "Could not find plaintext for'"  + string + "'."

def main():
    string = input("Enter md5 hash to find: ")
    print search(string)

if __name__ == "__main__":
    main()
