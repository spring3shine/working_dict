import bisect
import collections
import functools
import time
from typing import List


class Singleton(object):
    __instance = None

    def __init__(self):
        return

    def __new__(self,age,name):
        if not self.__instance:
            self.__instance = object.__new__(self)
        return self.__instance

if __name__ == '__main__':

    # print(Solution().search([1],0))
    # assert 1
    # collections.Counter
    # print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],1))

