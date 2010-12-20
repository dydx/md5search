#!/usr/bin/env python

''' Provides a facility for the generation of the file system '''

# done for all practical purposes

import hashlib
import os

def md5(string):
    return hashlib.md5(string).hexdigest()

# really dirty hack that I don't see a way around (immediately at least)
def traverse_to_basedir():
    traversal = ''
    for i in range(32):
        traversal += '../'
    os.chdir(traversal)

def create_plaintext(string):
    fd = open('plaintext.txt', 'w')
    fd.write(string)
    fd.close()

def create_entry(string):
    hash = md5(string)
    for index, character in enumerate(hash):
        if not os.path.exists(hash[index]):
            os.mkdir(hash[index])
            os.chdir(hash[index])
        else:
            os.chdir(hash[index])
    create_plaintext(string)
    traverse_to_basedir()

def create_filesystem():
    wordlist = input("Please enter the path to a valid wordlist: ")
    for word in open(wordlist,'r'):
        create_entry(word.rstrip())
    print "Done creating filesystem."

def main():
    create_filesystem()

if __name__ == "__main__":
    main()
