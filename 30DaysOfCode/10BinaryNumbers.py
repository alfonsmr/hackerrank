# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    max_ones = 0
    ones = 0
    bin_n = bin(n)[2:]

    for n in bin_n:
        if n == "1":
            ones += 1
        else:
            ones = 0
        if ones > max_ones:
            max_ones = ones

    print(max_ones)
        