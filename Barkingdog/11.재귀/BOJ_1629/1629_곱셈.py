"""
* CodingTest/Barkingdog/11(0x0B).재귀/BOJ_1629/1629_곱셈.py
* Author : mireutale
"""

# pow(a, b, c) = (a ** b) % c 를 계산해주는 파이썬 함수
import sys
input = lambda: sys.stdin.readline().rstrip()

def recursive(a, b, c):
    # ! 재귀
    # if b == 1:
    #     return a % c

    # half = recursive(a, b // 2, c)
    # if b % 2 == 0:
    #     return (half * half) % c
    # else:
    #     return (half * half * (a % c)) % c

    # ! 반복문
    result = 1
    a %= c

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = a ** 2 % c
        b //= 2
    
    return result


if __name__ == "__main__":
    a, b, c = map(int, input().split())    
    print(recursive(a, b, c))