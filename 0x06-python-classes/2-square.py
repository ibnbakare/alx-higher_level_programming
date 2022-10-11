#!/usr/bin/python3
class Square:
    '''
        defining square
    '''

    def __init__(self, size):
        '''
            intialization of instance attribute
            Args:
            size(int):0 or postive
        '''

        if not isinstance(size, int):
            raise TypeError("size must be integar")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
