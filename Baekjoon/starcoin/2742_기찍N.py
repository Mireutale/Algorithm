"""
* CodingTest/Starcoin/2742_기찍N.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    for i in range(n, 0, -1):
        print(i)