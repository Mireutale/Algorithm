"""
* Barkingdog\0x10 다이나믹프로그래밍\BOJ_2748\2748_피보나치수2.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input())
    fibo_list = [0] * (n+1)
    fibo_list[0] = 0
    fibo_list[1] = 1
    for i in range(2, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    print(fibo_list[n])