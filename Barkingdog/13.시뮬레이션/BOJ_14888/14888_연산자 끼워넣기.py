"""
* CodingTest/Barkingdog/13.시뮬레이션/BOJ_14888/14888_연산자 끼워넣기.py
* Author : mireutale
"""

import sys
from math import inf
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    op_cnts = list(map(int, input().split()))
    max_cnt = -inf
    min_cnt = inf
    symbols = ['+', '-', '*', '//']
    n = len(numbers)
    results = []

    def dfs(idx, path, counts):
        if idx == n - 1:
            results.append(path[:])
            return
        for i in range(4):
            if counts[i] > 0:
                counts[i] -= 1
                path.append(symbols[i])
                dfs(idx + 1, path, counts)
                path.pop()
                counts[i] += 1
    dfs(0, [], op_cnts)

    for ops in results:
        result = numbers[0]
        for i in range(n-1):
            op = ops[i]
            num = numbers[i+1]
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            else:
                if result < 0:
                    result = -(-result // num)
                else:
                    result //= num
        max_cnt = max(max_cnt, result)
        min_cnt = min(min_cnt, result)
    print(max_cnt)
    print(min_cnt)
