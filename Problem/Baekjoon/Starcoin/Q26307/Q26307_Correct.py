"""
* CodingTest/Starcoin/26307_Correct.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    HH, MM = map(int, input().split())
    hours = 60 * (HH - 9)
    minutes =  MM
    consumed = hours + minutes
    print(consumed)