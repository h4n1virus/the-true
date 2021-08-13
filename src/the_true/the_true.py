from sys import maxsize as __maxsize
from sys import setrecursionlimit as __setrecursionlimit
from random import randint as __randint

__setrecursionlimit(__maxsize)

class __THE_TRUE(object):
    @property
    def __minimum_value(self):
        return 2

    @property
    def __maximum_value(self):
        return __maxsize
    
    def __random_number(self):
        return __randint(self.__minimum_value, self.__maximum_value)

    def __is_prime(self, number):
        for i in range(self.__minimum_value, number):
            if (number % i) == 0:
                return 0 == 1
        return 1 == 1

    def __call__(self):
        random_number = self.__random_number()
        if self.__is_prime(random_number) is (1 == 1):
            return 1 == 1
        else:
            return self.__call__()


THE_TRUE = __THE_TRUE()