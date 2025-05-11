"""
* Codes\starcoin\2033_반올림.py
* Author : mireutale
"""


import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    divisor = 10
    
    while n > divisor:
        # divisor보다 한 자리수 작은 자리에서 반 올림
        remainder = n % divisor
        n -= remainder
        if int(str(remainder)[0]) >= 5:
            n += divisor
        divisor *= 10
    
    print(n)