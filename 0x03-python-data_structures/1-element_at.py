#!/usr/bin/python3
def element_at(my_list, idx):
    count = 1
    length = len(my_list)
    if idx < 0 or idx > int(length) -1:
        return (None)
    return (my_list[idx])

if __name__ == "__main__":
    print(element_at([1,3], 0))
