# Barkingdog/9.BFS&10.DFS/BOJ_3197/3197_백조의호수.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]
X : 얼어있는 공간
. : 물이 있는 공간
L : 백조가 있는 공간

물이 있는 공간과 접촉한 얼어있는 공간(빙판)은 매일 녹는다.
두마리의 백조가 몇일 후 만날 수 있는지 구하시오.

처음 만나는 백조를 swan에 넣고, 두번째 백조의 위치를 dest로 설정
처음 물인 상태의 위치를 water, 물과 인접해 있어 다음날 녹을 빙판의 위치를 melt_place
현재 백조를 이동시키고, 백조가 만날수 있는 빙판은 다음날 물이 될 것이므로 다음날 백조가 확인해봐야할 tomorrow_swan에 저장

백조의 이동 경로에서, 물은 그대로 swan에 넣고, 빙판만 tomorrow_swan에 추가

메모리를 아끼기 위해서 water와 melt_place / swan과 tomorrow_swan을 하루 탐색이 끝나고 swap

목적지에 백조가 도달할 수 있다면 그날의 시간을 출력
"""
def melt(dir, r, c):
    # 물의 위치에 따라서, 
    while water:
        x, y = water.popleft()
        # melt_place가 water이 되어서 꺼내질때, 빈 공간으로 변경
        lake[x][y] = "."
        for i in range(4):
            nx, ny = x + dir[i][0], y + dir[i][1]
            if 0 <= nx < r and 0 <= ny < c and not water_visited[nx][ny]:
                # 물과 만나는 빙판
                if lake[nx][ny] == "X":
                    water_visited[nx][ny] = True
                    melt_place.append([nx, ny])

def move_swan(dir, r, c):
    while swan:
        x, y = swan.popleft()
        # 목적지를 백조가 이동 가능하면 완료
        if x == destX and y == destY:
            return True
        
        for i in range(4):
            nx, ny = x + dir[i][0], y + dir[i][1]
            if 0 <= nx < r and 0 <= ny < c and not swan_visited[nx][ny]:
                    # 다음날 백조가 탐색해야할 빙판
                    if lake[nx][ny] == "X":
                        tomorrow_swan.append([nx, ny])
                    # 빈 공간은 이동 가능하므로, 백조의 위치에 추가
                    elif lake[nx][ny] == ".":
                        swan.append([nx, ny])
                    swan_visited[nx][ny] = True
    return False

if __name__ == "__main__":
    r, c = map(int, input().split())
    lake = [list(input()) for _ in range(r)] # 호수의 상태
    water_visited = [[False]*c for _ in range(r)]
    swan_visited = [[False]*c for _ in range(r)]

    swan = deque() # 백조의 위치 저장
    water = deque() # 물의 위치 저장
    melt_place = deque() # 녹을 빙판의 위치 저장
    tomorrow_swan = deque() # 다음날 백조가 추가로 이동 가능한 위치

    for i in range(r):
        for j in range(c):
            if lake[i][j] == "L": # 백조를 만난 경우
                if not swan: # swan이 빈 경우, 처음 만난 백조
                    swan.appendleft([i, j]) # 백조 저장
                    swan_visited[i][j] = True
                else: # 두번째 백조
                    destX, destY = i, j # 목적지로 설정
                # 모든 백조를 물로 바꿈
                lake[i][j] == "."
                water.append([i, j])
                water_visited[i][j] = True
            elif lake[i][j] == ".": # 물을 만난 경우
                water.append([i, j]) # 물 저장
                water_visited[i][j] = True

    dir = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 방향
    time = 0 # 날짜

    while True:
        # 녹는 빙판 찾기
        melt(dir, r, c)
        # 백조 이동, 다음번에 봐야할 백조의 빙판
        if move_swan(dir, r, c):
            # 만약 다른 백조를 찾은 경우
            print(time)
            break
        #swan과 water는 빈 deque이므로 메모리 낭비가 없게 하기 위해서
        #swan과 tomorrow_swan / water melt_place를 swap
        swan, tomorrow_swan = tomorrow_swan, swan
        water, melt_place = melt_place, water
        # 다음날
        time += 1
