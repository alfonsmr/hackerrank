# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for x in range(1,11):
        print ("{} x {} = {}".format(n,x,n*x))