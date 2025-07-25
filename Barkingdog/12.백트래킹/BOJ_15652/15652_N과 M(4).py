"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_15652/15652_N과 M(4).py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = []

    def back_tracking():
        if len(ans) == m:
            print(*ans)
            return
        
        for i in range(1, n + 1):
            if not ans or ans[-1] <= i:
                ans.append(i)
                back_tracking()
                ans.pop()

    back_tracking()