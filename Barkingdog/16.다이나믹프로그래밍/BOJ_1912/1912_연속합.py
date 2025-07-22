"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_1912/1912_연속합.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(1, len(numbers)):
        # * 이전까지의 최대값 + 현재값 vs 현재값 비교
        numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])
    print(max(numbers))