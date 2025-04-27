#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]

불은 동서남북 빈 공간으로 퍼지고, 벽에는 불이 붙지 않음
사람은 동서남북 인접한 칸으로 이동 가능하며 1초가 걸림
사람이 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동 가능
빌딩을 얼마나 빨리 탈출할 수 있는지?

"." : 빈 공간
"#" : 벽
"@" : 시작 위치
"*" : 불
"""
def start_and_fire_position(building, m, n):
    fire_and_start = deque()
    for i in range(n):
        for j in range(m):
            if building[i][j] == "@":
                fire_and_start.append([i, j, 0])
                break
    for i in range(n):
        for j in range(m):
            if building[i][j] == "*":
                fire_and_start.append([i, j, 0])
    return fire_and_start

def escape(building, m, n, list_of_fire_and_start):
    queue = list_of_fire_and_start

    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    while queue:
        x, y, time = queue.popleft()
        # 탈출 직전인 경우
        if building[x][y] == "@":
            if x == 0 or x+1 == n:
                time += 1
                return time
            elif y == 0 or y+1 == m:
                time += 1
                return time

        # 빌딩 안인 경우, 불과 현재 위치를 이동
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < m and building[nx][ny] != "#":
                # 현재 위치의 경우, 빈 공간으로 만 이동
                if building[x][y] == "@":
                    if building[nx][ny] == ".":
                        queue.append([nx, ny, time+1])
                        building[nx][ny] = "@"
                # 불의 경우 @와 빈 공간으로 번지는게 가능
                elif building[x][y] == "*":
                    if building[nx][ny] == "@" or building[nx][ny] == ".":
                        queue.append([nx, ny, time+1])
                        building[nx][ny] = "*"

    return "IMPOSSIBLE"

if __name__ == "__main__":
    test_case_count = int(input())
    for _ in range(test_case_count):
        m, n = map(int, input().split())
        building = list(list(input()) for _ in range(n))
        list_of_fire_and_start = start_and_fire_position(building, m, n)
        print(escape(building, m, n, list_of_fire_and_start))