"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_15650/15650_N과 M(2).py
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
            if (i) not in ans:
                # 오름차순, 즉 현재 들어있는 값보다 i가 커야만 append
                if not ans or ans[-1] < i:
                    ans.append(i)
                    back_tracking()
                    ans.pop()

    back_tracking()