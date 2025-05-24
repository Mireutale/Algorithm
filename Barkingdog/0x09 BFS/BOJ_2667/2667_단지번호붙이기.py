#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]
1은 집이 있는 곳, 0은 집이 없는 곳을 나타냄
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의 및 단지에 번호를 붙인다.

연결 : 상하좌우에 다른 집이 있는 경우
"""
def search(n, count, board, x, y, visited):
    queue = deque([(x, y)])
    area = 1
    visited[x][y] = True
    board[x][y] = count

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위내에 있고, queue에 들어가 있지 않은 집을 찾아서 추가
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and not visited[nx][ny]:
                queue.append([nx, ny])
                area += 1
                visited[nx][ny] = True
                board[nx][ny] = count
    return area

if __name__ == "__main__":
    n = int(input()) # (5 ~ 25) N * N 크기의 지도의 한 변
    board = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    count = 0 #총 단지수
    houses = []
    for i in range(n):
        for j in range(n):
            # 집인 경우
            if board[i][j] != 0 and not visited[i][j]:
                # 단지 추가
                count += 1
                # 단지의 집 개수 확인 및 추가
                houses.append(search(n, count, board, i, j, visited))
    print(count)
    houses.sort()
    print(*houses, sep="\n")