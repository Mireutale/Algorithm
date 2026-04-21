# Barkingdog/16.다이나믹프로그래밍/BOJ_11727/11727_2xn타일링2.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    count = [1] * (n+1)
    count[1] = 1
    for i in range(2, n+1):
        count[i] = count[i-1] + count[i-2] * 2
    print(count[n] % 10007)
