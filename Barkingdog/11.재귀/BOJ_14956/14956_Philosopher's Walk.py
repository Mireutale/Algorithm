# Barkingdog/11.재귀/BOJ_14956/14956_Philosopher's Walk.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def Philosophers_walk(n, m):
    # Base case: n == 2일 때 직접 좌표 반환
    if n == 2:
        move = [(1, 1), (1, 2), (2, 2), (2, 1)]
        return move[m - 1]

    side = n // 2
    area = side**2

    if m <= area:
        x, y = Philosophers_walk(side, m)
        return (y, x)
    elif m <= 2 * area:
        x, y = Philosophers_walk(side, m - area)
        return (x, y + side)
    elif m <= 3 * area:
        x, y = Philosophers_walk(side, m - 2 * area)
        return (x + side, y + side)
    else:
        x, y = Philosophers_walk(side, m - 3 * area)
        return (2 * side - y + 1, side - x + 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    x, y = Philosophers_walk(n, m)
    print(x, y)
