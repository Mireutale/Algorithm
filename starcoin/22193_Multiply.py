"""
* CodingTest/starcoin/22193_Multiply.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = int(input())
    b = int(input())
    print(a*b)