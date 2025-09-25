"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_18809/18809_Gaaaaaaaaaarden.py
* Author : mireutale
"""

import sys
from itertools import combinations
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# def combinations(arr, r):
#     result = []

#     def backtrack(start, path):
#         if len(path) == r:
#             result.append(path[:])  # 조합 하나 완성
#             return
#         for i in range(start, len(arr)):
#             path.append(arr[i])
#             backtrack(i + 1, path)
#             path.pop()

#     backtrack(0, [])
#     return result

def backTracking(red, green):
    # 배양액 퍼뜨리기
    q = deque()
    # 배양액을 떨어트린 시간을 가짐
    red_map = [[-1] * M for _ in range(N)]
    green_map = [[-1] * M for _ in range(N)]
    flower_map = [[0] * M for _ in range(N)]

    # 초기 위치를 0으로 지정
    for x, y in red:
        q.append((x, y, 'R', 0))
        red_map[x][y] = 0

    for x, y in green:
        q.append((x, y, 'G', 0))
        green_map[x][y] = 0

    flower = 0
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    # q는 배양액의 위치를 가지고 있음.
    while q:
        next_q = deque()

        while q:
            x, y, color, t = q.popleft()

            # 이미 꽃이 핀 곳은 skip
            if flower_map[x][y]:
                continue

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if garden[nx][ny] == 0:
                    continue
                if flower_map[nx][ny]:
                    continue

                if color == 'R':
                    if red_map[nx][ny] == -1 and green_map[nx][ny] == -1:
                        red_map[nx][ny] = t + 1
                        next_q.append((nx, ny, 'R', t + 1))

                elif color == 'G':
                    if green_map[nx][ny] == -1:
                        if red_map[nx][ny] == t + 1:  # 동시에 도착 → 꽃 핌
                            flower += 1
                            flower_map[nx][ny] = 1
                        elif red_map[nx][ny] == -1:
                            green_map[nx][ny] = t + 1
                            next_q.append((nx, ny, 'G', t + 1))
        q = next_q
    return flower

def perDay():
    global ans
    for selected in combinations(candidate, R + G):
        for red in combinations(selected, R):
            green = [pos for pos in selected if pos not in red]
            flowers = backTracking(red, green)
            ans = max(ans, flowers)

if __name__ == "__main__":
    N, M, G, R = map(int, input().split())
    # 0은 호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴 수 있는 땅
    garden = []
    candidate = []
    ans = 0
    for i in range(N):
        row = list(map(int, input().split()))
        garden.append(row)
        for j in range(M):
            if row[j] == 2:
                candidate.append((i, j)) # 배양액 뿌릴 수 있는 위치 저장

    perDay()
    print(ans)