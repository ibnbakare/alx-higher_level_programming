#!/usr/bin/python3
class Square:
    '''
        defining square
    '''

    def __init__(self, size):
        '''
            initialization of instance attribute
            Args:
            size(int):0 or positive
        '''

        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
