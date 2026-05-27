# Barkingdog/11.재귀/BOJ_11729/11729_하노이탑이동순서.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def hanoi(n: int, start: int, end: int):
    if n == 1:
        ans.append([start, end])
        return
    else:
        temp = 6 - start - end
        hanoi(n-1, start, temp)
        ans.append([start, end])
        hanoi(n-1, temp, end)

if __name__ == "__main__":
    n = int(input())
    ans = []
    hanoi(n, 1, 3)
    print(len(ans))
    for row in ans:
        print(*row)
