"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_15657/15657_N과 M(8).py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))
    ans = []

    def back_tracking():
        if len(ans) == m:
            print(*ans)
            return
        
        for i in sorted(number_list):
            if not ans or ans[-1] <= i:
                ans.append(i)
                back_tracking()
                ans.pop()

    back_tracking()