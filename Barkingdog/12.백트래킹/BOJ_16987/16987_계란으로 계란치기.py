"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_15665/15665_N과 M(11).py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    eggs = int(input())
    durability = []
    weight = []
    for _ in range(eggs):
        d, w = map(int, input().split())
        durability.append(d)
        weight.append(w)
    max_broken_egg = 0

    def breaking_egg(index: int = 0):
        global max_broken_egg
        if index == eggs:
            broken_egg = sum(1 for i in range(eggs) if durability[i] <= 0)
            max_broken_egg = max(max_broken_egg, broken_egg)
            return

        is_hit = False
        for i in range(eggs):
            if i == index or durability[i] <= 0:
                continue

            if durability[index] <= 0:
                continue

            is_hit = True
            durability[index] -= weight[i]
            durability[i] -= weight[index]

            breaking_egg(index + 1)

            durability[index] += weight[i]
            durability[i] += weight[index]

        if not is_hit:
            breaking_egg(index + 1)

    breaking_egg()
    print(max_broken_egg)
