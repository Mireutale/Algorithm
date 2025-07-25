"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_15665/15665_N과 M(11).py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))
    number_list.sort()
    ary = []

    """set을 활용한 중복 제거"""
    ans = set()
    
    def back_tracking():
        if len(ary) == m:
            temp = tuple(ary)
            if temp not in ans:
                print(*ary)
                ans.add(temp)
            return
        
        for i in range(len(number_list)):
            ary.append(number_list[i])
            back_tracking()
            ary.pop()

    back_tracking()