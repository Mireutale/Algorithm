# Barkingdog/12.백트래킹/BOJ_1182/1182_부분수열의 합.py

import sys
input = lambda: sys.stdin.readline().rstrip()

ans = 0

if __name__ == "__main__":
    n, s = map(int, input().split())
    num = list(map(int, input().split()))
    sub_num = []
    
    def back_tracking(start):
        global ans
        if sum(sub_num) == s and len(sub_num) > 0:
            ans += 1
        for i in range(start, n):
            sub_num.append(num[i])
            back_tracking(i+1)
            sub_num.pop()
    
    back_tracking(0)
    print(ans)
