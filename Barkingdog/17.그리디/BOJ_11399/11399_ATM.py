# Barkingdog/17.그리디/BOJ_11399/11399_ATM.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n = int(input())
    p = map(int, input().split())
    p = deque(sorted(p))

    last = 0
    total = 0

    while p:
        last += p.popleft()
        total += last
        
    print(total)