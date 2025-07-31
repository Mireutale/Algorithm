"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_11659/11659_구간합구하기4.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = deque(map(int, input().split()))
    for i in range(1, n):
        numbers[i] += numbers[i-1]
    numbers.appendleft(0)
    # print(numbers)
    for _ in range(m):
        i, j = map(int, input().split())
        print(numbers[j] - numbers[i-1])