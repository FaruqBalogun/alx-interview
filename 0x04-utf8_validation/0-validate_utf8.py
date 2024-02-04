#!/usr/bin/python3
"""UTF-8 Validation"""


def getNumOfOnes(num):
    if (num & 0b10000000) == 0:
        return 1
    elif (num & 0b11100000) == 0b11000000:
        return 2
    elif (num & 0b11110000) == 0b11100000:
        return 3
    elif (num & 0b11111000) == 0b11110000:
        return 4
    else:
        return False


def validUTF8(data):
    i = num_of_ones = 0

    while i < len(data):
        num = data[i]

        num_of_ones = getNumOfOnes(num)
        if not num_of_ones:
            return False

        if i + num_of_ones > len(data):
            return False

        while num_of_ones > 1:
            i += 1
            if (data[i] & 0b11000000) != 0b10000000:
                return False
            num_of_ones -= 1

        i += 1

    return True