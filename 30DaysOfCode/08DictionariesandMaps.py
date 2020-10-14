# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

#!/bin/python3

# The first line contains an integer, , denoting the number of entries in the phone book.
# Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line.
# The first value is a friend's name, and the second value is an -digit phone number.
# After the  lines of phone book entries, there are an unknown number of lines of queries. 
# Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break