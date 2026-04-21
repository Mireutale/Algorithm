# Barkingdog/13.시뮬레이션/BOJ_15686/15686_치킨배달.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def chicken_delivery(depth, n):
    global ans
    ret = 0
    if depth == m:
        for d in distance:
            for dist, index in d:
                if visited[index]:
                    ret += dist
                    break
            if ans <= ret:
                return
        ans = min(ans, ret)
        return

    for i in range(n, len(chickens)):
        if not visited[i]:
            visited[i] = 1
            chicken_delivery(depth + 1, i + 1)
            visited[i] = 0
    return

# * 백트래킹
if __name__ == "__main__":
    n, m = map(int, input().split())
    city =[list(map(int, input().split())) for _ in range(n)]
    houses = []
    chickens = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    distance = []
    for hx, hy in houses:
        distance.append([])
        for idx, c in enumerate(chickens):
            cx, cy = c
            distance[-1].append((abs(hx-cx) + abs(hy-cy), idx))
        distance[-1].sort()
    ans = float('inf')
    visited = [0 for _ in range(len(chickens))]
    chicken_delivery(0, 0)
    print(ans)

# * 이중 포문
"""
import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    houses = []
    chickens = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j, value in enumerate(row):
            if value == 1:
                houses.append((i, j))
            elif value == 2:
                chickens.append((i, j))

    distance = [[abs(cx-hx) + abs(cy-hy) for (cx, cy) in chickens] for (hx, hy) in houses]
        
    ans = float('inf')
    
    for comb in combinations(range(len(chickens)), m): # m개의 치킨집 선택
        total = 0
        for h in range(len(houses)):
            # 해당 집의 최소 치킨 거리
            total += min(distance[h][c] for c in comb)
            if total >= ans: # 기존에 저장된 값보다 커지면 확인할 필요 없음
                break
        ans = min(ans, total)
    print(ans)
"""
