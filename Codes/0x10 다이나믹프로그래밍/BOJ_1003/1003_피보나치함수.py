"""
* Codes\0x10 다이나믹프로그래밍\BOJ_1003\1003_피보나치함수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        fibo = [0] * (n+2)
        fibo[0] = 0
        fibo[1] = 1
        for i in range(2, n+1):
            fibo[i] = fibo[i-1] + fibo[i-2]
        print(fibo[n-1], fibo[n])