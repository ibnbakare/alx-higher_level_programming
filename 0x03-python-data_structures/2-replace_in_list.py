#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx > 0) and (idx < int(length) - 1):
        my_list[idx] = element
        return(my_list)
    else:
        return (None)
if __name__ == "__main__":
    my_list =[1,2,3,4]
    print(replace_in_list(my_list,4,2))
