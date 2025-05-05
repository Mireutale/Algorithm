"""
* Codes/starcoin/26532_Acres.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
import math

if __name__ == "__main__":
    m, n = map(int, input().split())
    acres = (m * n) / 4840
    print(math.ceil(acres / 5))