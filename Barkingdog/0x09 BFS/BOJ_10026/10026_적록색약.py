"""
* Barkingdog\0x09 BFS\BOJ_10026\10026_적록색약.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못함 -> 빨간색과 초록색을 동일한 색상으로 판단

같은 구역 -> 같은 색상이 상하좌우로 인접해 있는 경우

적록색약인 사람, 적록색약이 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램
"""
def search_area(board, x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if board[x][y] == board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    
    return 1

def red_green_color_blindness_search_area(board, x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                # B구역인 경우
                if board[x][y] == 'B':
                    if board[nx][ny] == 'B' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                # R, G구역인 경우
                else:
                    if board[nx][ny] != 'B' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
    
    return 1


if __name__ == "__main__":
    n = int(input())
    board = [list(input()) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    area = 0
    red_green_color_blindness_visited = [[False]*n for _ in range(n)]
    red_green_color_blindness_area = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                area += search_area(board, i, j, visited)
            if not red_green_color_blindness_visited[i][j]:
                red_green_color_blindness_area += red_green_color_blindness_search_area(board, i, j, red_green_color_blindness_visited)

    print(area, red_green_color_blindness_area)

"""
다른 풀이
search_area 수행 -> 일반인의 구역 발견
후 2중 for문을 돌면서 G를 모두 R로 변경
이후 다시 search_area를 수행 -> 적록색약의 구역 발견
정답제출
"""