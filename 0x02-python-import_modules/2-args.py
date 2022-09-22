#!/usr/bin/python3
from sys import argv
def arguments():
    

    lenght = len(argv) - 1
    if lenght == 0:
        print("{} arguments".format(lenght))
    elif lenght == 1:
        print("{} argument:".format(lenght))
        print("{}: argument".format(argv[1]))
    elif lenght > 1:
        print("{} argument:".format(lenght))
        count = 1
        for r in argv[1:]:
            print("{}: {}".format(count, r))
            count += 1
if __name__ == "__main__":
    
    arguments()
