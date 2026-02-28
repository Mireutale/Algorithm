"""
* Codes\starcoin\6840_Whoisinthemiddle?.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

first = int(input())
second = int(input())
third = int(input())

bears = [first, second, third]
print(sorted(bears)[1])
