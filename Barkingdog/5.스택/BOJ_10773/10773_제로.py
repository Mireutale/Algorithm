# Barkingdog/5.스택/BOJ_10773/10773_제로.py

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
정수 K가 주어짐(1 ~ 100,000)
K개의 줄에 정수가 1개씩 주어진다.
정수는 (1 ~ 1,000,000)사이의 값을 가지며, 정수가 0인 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 씀
정수가 0인 경우 지울 수 있는 수가 반드시 있음.

모든 정수의 합을 구하라.
"""

if __name__ == "__main__":
    K = int(input())
    numbers = []
    for _ in range(K):
        ints = int(input())
        if ints == 0:
            numbers.pop()
        else:
            numbers.append(ints)
    print(sum(numbers))
