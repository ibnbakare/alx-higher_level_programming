#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        print(i)


if __name__ == "__main__":
    print_reversed_list_integer([1, 4])
