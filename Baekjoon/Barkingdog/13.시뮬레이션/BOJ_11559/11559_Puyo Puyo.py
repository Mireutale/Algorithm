# Barkingdog/13.시뮬레이션/BOJ_11559/11559_Puyo Puyo.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def print_board():
    for i in range(12):
        print(board[i])

def check(x, y) -> list:
    next_point = deque()
    next_point.append([x, y])
    visited[x][y] = True
    puyo_list = deque([(x, y)])
    while next_point:
        x, y = next_point.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if (0 <= nx < 12) and (0 <= ny < 6) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                puyo_list.append([nx, ny])
                next_point.append([nx, ny])
    
    return puyo_list

# 동일한 색 4개 이상이 이어진 puyo_list의 puyo를 터트림
def boom(puyo_list):
    for x, y in puyo_list:
        board[x][y] = '.'

# 남은 puyo를 아래로 이동
def down():
    for i in range(6-1, -1, -1):
        blank = deque()
        for j in range(12-1, -1, -1):
            # 가장 아래부터, 빈 공간 체크
            if board[j][i] != '.':
                blank.append(board[j][i])
                board[j][i] = '.'
        
        high = 11
        while blank:
            board[high][i] = blank.popleft()
            high -= 1

if __name__ == "__main__":
    # 뿌요 모습 저장
    board = [list(input()) for _ in range(12)]
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    combo = 0

    # 전체 블록 확인
    while True:
        delete = False
        visited = [[False] * 6 for _ in range(12)]
        puyo_list = deque()

        for i in range(12-1, -1, -1):
            for j in range(6-1, -1, -1):
                if board[i][j] != '.' and not visited[i][j]:
                    puyo_list = check(i, j)
                    if len(puyo_list) >= 4:
                        delete = True
                        boom(puyo_list)
        
        if delete:
            combo += 1
            down()
        else:
            break

    print(combo)