from sys import maxsize
from random import randint


class __THE_TRUE(object):
    @property
    def __minimum_value(self):
        return 2

    @property
    def __maximum_value(self):
        return maxsize
    
    def __random_number(self):
        return randint(self.__minimum_value, self.__maximum_value)

    def __is_prime(self, number):
        for i in range(self.__minimum_value, int(number ** 0.5)):
            if (number % i) == 0:
                return 0 == 1
        return 1 == 1

    def is_prime_primality_test(self, number):
        pass

    def __call__(self):
        random_number = self.__random_number()
        if self.__is_prime(random_number) is (1 == 1):
            return 1 == 1
        else:
            return self.__call__()


THE_TRUE = __THE_TRUE()
