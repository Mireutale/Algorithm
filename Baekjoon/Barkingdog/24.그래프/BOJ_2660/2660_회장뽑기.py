# Barkingdog/24.그래프/BOJ_2660/2660_회장뽑기.py

import sys
import math
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    friends = [[] for _ in range(n)]
    while True:
        x, y = list(map(int, input().split()))
        
        if x == -1 and y == -1:
            break
        
        friends[x-1].append(y-1)
        friends[y-1].append(x-1)
    
    far = [[50]*n for _ in range(n)]
    for index, friend in enumerate(friends):
        far[index][index] = 0
        for who in friend:
            far[index][who] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                far[i][j] = min(far[i][j], far[i][k] + far[k][j])
    
    min_depth = 50
    candidate = []
    for idx,row in enumerate(far):
        if max(row) < min_depth:
            candidate.clear()
            min_depth = max(row)
            candidate.append(idx+1)
        elif max(row) == min_depth:
            candidate.append(idx+1)

    print(min_depth, len(candidate))
    print(*candidate)

