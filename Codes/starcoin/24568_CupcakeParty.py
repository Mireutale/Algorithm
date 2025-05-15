"""
* Codes\starcoin\24568_CupcakeParty.py
* Author : mireutale
"""


import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    r = int(input()) # 8 cupcakes
    s = int(input()) # 3 cupcakes
    total = 8*r + 3*s
    print(total-28)