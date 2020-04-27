'''
Задача 3
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

from math import *


def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    for y in range(3, ceil(sqrt(x)) + 1, 2):
        if x % y == 0:
            return False

    return True


def largest_prime_number(number):
    for x in range(ceil(sqrt(number)), 0, -1):
        if number % x == 0 and is_prime(x):
            return x
    return None

print(largest_prime_number(600851475143))