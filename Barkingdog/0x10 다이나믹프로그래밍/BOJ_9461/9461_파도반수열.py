"""
* Barkingdog\0x10 다이나믹프로그래밍\BOJ_9461\9461_파도반수열.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    test_case = int(input())
    P = [0] * 101
    P[1] = 1
    P[2] = 1
    P[3] = 1
    P[4] = 2
    P[5] = 2
    P[6] = 3
    for i in range(7, 101):
        P[i] = P[i-1] + P[i-5]
    for _ in range(test_case):
        n = int(input())
        print(P[n])