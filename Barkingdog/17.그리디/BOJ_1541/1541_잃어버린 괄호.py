# Barkingdog/17.그리디/BOJ_1541/1541_잃어버린 괄호.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def split_plus(data):
    if '+' in data:
        need_to_sum = map(int, data.split('+'))
        data = sum(need_to_sum)
    return int(data)

if __name__ == "__main__":
    exp = input().split('-')
    exp = deque(exp)

    total = int(split_plus(exp.popleft()))
    while exp:
        x = split_plus(exp.popleft())
        total -= int(x)
    print(total)