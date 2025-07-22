"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_6593/6593_상범빌딩.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]

빌딩은 각 변의 길이가 1인 정육면체로 이루어져 있음
인접한 6곳(앞, 뒤, 상, 하, 좌, 우)로 1분의 시간을 들여 이동 가능
탈출하는 가장 빠른 길은 무엇인가?

# -> 막혀서 지나갈 수 없는 칸
. -> 비어 있어서 이동 가능한 칸
"""
def bfs(building, L, R, C):
    queue = deque()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    building[i][j][k] = 0
                    queue.append([i, j, k])
                    break
    
    direction = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
    find = False
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + direction[i][0], y + direction[i][1], z + direction[i][2]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if building[nx][ny][nz] == '.':
                    building[nx][ny][nz] = building[x][y][z] + 1
                    queue.append([nx, ny, nz])
                if building[nx][ny][nz] == 'E':
                    find = building[x][y][z] + 1
                    break
    return find


if __name__ == "__main__":
    # 1 ~ L ~ 30 -> 상범 빌딩의 층 수
    # 1 ~ R, C ~ 30 -> 빌딩 한 층의 행과 열 개수
    while True:
        L, R, C = map(int, input().split())
        if L == 0 and R == 0 and C == 0:
            exit()
        building = []
        for _ in range(L):
            floor = []
            for _ in range(R + 1):
                row = input()
                if row:  # 빈 문자열이 아닌 경우에만 추가
                    floor.append(list(row))
            building.append(floor)
        ans = bfs(building, L, R, C)
        if not ans:
            print("Trapped!")
        else:
            print('Escaped in', ans, "minute(s).")
# commit msg
# --- 문제풀이_mireutale[25/ / ]