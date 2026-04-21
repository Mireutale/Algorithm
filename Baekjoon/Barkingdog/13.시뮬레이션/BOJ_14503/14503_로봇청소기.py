# Barkingdog/13.시뮬레이션/BOJ_14503/14503_로봇청소기.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split()) # * d = 0, 1, 2, 3 = N, E, S, W
    room = [list(map(int, input().split())) for _ in range(N)]
    clean = 0
    while True:
        # print(r, c, clean, d)
        # print(*room, sep="\n")
        # 1. 현재 칸 청소
        if room[r][c] == 0:
            clean += 1
            room[r][c] = 2
            continue

        # 2. 주변 4칸 중 청소되지 않은 칸 탐색
        moved = False
        for _ in range(4):
            d = (d + 3) % 4 # 3, 2, 1, 0 -> 반시계 반복
            nr, nc = r + direction[d][0], c + direction[d][1]
            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] == 0:
                    r, c = nr, nc # 앞으로 이동
                    moved = True
                    break
        if moved:
            continue

        # 3. 뒤로 이동
        br, bc = r - direction[d][0], c - direction[d][1]
        if not (0 <= nr < N and 0 <= nc < M) or room[br][bc] == 1:
            break # 막혀있으면 중지
        r, c = br, bc # 뒤로이동

    print(clean)
