"""
* CodingTest\Barkingdog\starcoin\26082_WARBOY.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    another = b//a
    print(another*3*c)