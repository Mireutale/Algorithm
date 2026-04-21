"""
* CodingTest/Starcoin/26560_Periods.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        sentence = input()
        if sentence[-1] != ".":
            sentence += "."
        print(sentence)