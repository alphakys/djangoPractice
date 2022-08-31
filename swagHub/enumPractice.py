import enum
import string
from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


print(Color.BLUE)
print(repr(Color.RED))
print(type(Color))
print(repr(Color.BLUE.value))


class Shake(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    COOKIES = 3
    MINT = 4


print(Shake['VANILLA'])

# print(type(Shake.VANILLA))
# for s in Shake:
#     print('test : ', end='')
#     if s.name.__eq__('VANILLA'):
#         print('v')

#
# apples = {}
# print(type(apples))
#
# apples[Shake.VANILLA] = 'I like vanilla'
# apples[1] = Shake.MINT
#
#
# print(apples)














