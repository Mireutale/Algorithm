import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]
1층 빌딩 -> 열쇠가 있어야 문을 열 수 있음
일부 열쇠는 가지고 있으며, 일부 열쇠는 빌딩의 바닥에 놓여져 있음.
상하좌우로 이동 가능, 훔칠 수 있는 문서의 최대 개수를 구하시오

"." : 빈 공간
"*" : 벽
"$" : 훔쳐야 하는 문서
알파벳 대문자 : 문
알파벳 소문자 : 열쇠

visited를 활용하지 않는 경우 -> 틀림
? building의 값을 *벽으로 바꾸어서 처리하려고 하니 문제 발생
! visited를 활용해서 재 방문을 처리하자
"""
def find_inputs(building, keys, h, w, doors):
    input_position = deque()
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if not building[i][j] == "*":
                    if building[i][j] == ".":
                        input_position.append([i, j])
                    elif 'A' <= building[i][j] <= 'Z':
                        if building[i][j].lower() in keys:
                            input_position.append([i, j])
                        else:
                            doors[building[i][j]].append((i, j))
                    elif building[i][j] == "$":
                        input_position.append([i, j])
                    else:
                        input_position.append([i, j])
                        keys.add(building[i][j])
    return input_position, doors, keys

def find_document_steal(building, input_position, keys, h, w, doors):
    queue = input_position
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[False] * w for _ in range(h)]
    document = 0

    for x, y in queue:
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        # $를 만난 경우
        if building[x][y] == "$":
            document += 1

        # 현재 위치가 열쇠 -> 키에 새로 값을 추가하고 문들 중에서 열 수 있는지 확인
        if 'a' <= building[x][y] <= 'z':
            new_key = building[x][y]
            keys.add(new_key)
            if new_key.upper() in doors:
                for dx, dy in doors[new_key.upper()]:
                    if not visited[dx][dy]:
                        queue.append((dx, dy))
                        visited[dx][dy] = True

        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            # 범위 내, 아직 지나지 않은 위치
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                # 빈 공간이나 문서
                if building[nx][ny] == "." or building[nx][ny] == "$":
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                # 문을 만난 경우
                elif 'A' <= building[nx][ny] <= 'Z':
                    # 열쇠가 있으면 바로 queue에 추가
                    if building[nx][ny].lower() in keys:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                    # 열쇠가 없으면 열지 못하는 문에 추가
                    else:
                        doors[building[nx][ny]].append((nx, ny))
                # 열쇠를 만난 경우
                elif 'a' <= building[nx][ny] <= 'z':
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return document

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        h, w = map(int, input().split())
        building = [list(input()) for _ in range(h)]
        key = input()
        keys = set(key) if key != '0' else set()
        # 알파벳 딕셔너리 생성
        doors = {chr(i): deque() for i in range(65, 91)}  # A-Z
        input_position, doors, keys = find_inputs(building, keys, h, w, doors)
        if not input_position:
            print(0)
        else:
            print(find_document_steal(building, input_position, keys, h, w, doors))
