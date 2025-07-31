"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_15649/15649_N과 M(1).py
* Author : mireutale
"""

import sys
# import itertools import permutaions
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = []

    def back_tracking():
        if len(ans) == m:
            print(*ans)
            return
        
        for i in range(n):
            if (i+1) not in ans:
                ans.append(i+1)
                back_tracking()
                ans.pop()

    back_tracking()
    # ans = permutation(range(1, n+1), m)
    # print(*ans)