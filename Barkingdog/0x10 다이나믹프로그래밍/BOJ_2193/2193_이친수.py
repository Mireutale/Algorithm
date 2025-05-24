"""
* Barkingdog\0x10 다이나믹프로그래밍\BOJ_2193\2193_이친수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    pinary = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1:
            pinary[i] = 1
        else:
            pinary[i] = pinary[i-1] + pinary[i-2]
    print(pinary[n])