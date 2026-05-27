# Barkingdog/12.백트래킹/BOJ_1941/1941_소문난 칠공주.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    girls_class = [input().strip() for _ in range(5)]
    ans = 0

    selected = []
    visited = set()

    def is_valid():
        # 인접 확인 & S 개수 확인
        queue = deque()
        queue.append(selected[0])
        seen = set() # 시작점별, 방문했는지 확인하는 값
        seen.add(selected[0])
        s_count = 0
        # x = selected[0] // 5
        # y = selected[0] % 5
        x, y = divmod(selected[0], 5)
        if girls_class[x][y] == 'S':
            s_count += 1

        connected = 1
        while queue:
            current = queue.popleft()
            x, y = divmod(current, 5)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5:
                    ni = nx * 5 + ny
                    if ni in selected and ni not in seen:
                        seen.add(ni) # 방문 위치 저장
                        queue.append(ni) # 이동 위치 추가
                        connected += 1
                        if girls_class[nx][ny] == 'S':
                            s_count += 1
        return connected == 7 and s_count >= 4

    def seven_princess(start, depth, y_count, selected):
        global ans
        if y_count >= 4:  # Y가 4명이면 탈락 조건
            return

        if depth == 7:
            if is_valid(selected):
                ans += 1
            return

        for i in range(start, 25):
            if i not in visited:
                selected.append(i)
                x, y = divmod(i, 5)
                seven_princess(i + 1, depth + 1, y_count + 1)
                selected.remove(i)

    # 호출 시 초기값 추가
    seven_princess(0, 0, 0)
    print(ans)
    """

    # 최적화 -> visited 삭제, if문 간결하게 변경
    girls_class = [input().strip() for _ in range(5)]
    ans = 0

    def is_valid(selected):
        selected = list(selected)
        queue = deque([selected[0]])
        seen = set([selected[0]])
        s_count = 0

        x, y = divmod(selected[0], 5)
        if girls_class[x][y] == 'S':
            s_count += 1

        connected = 1
        while queue:
            curr = queue.popleft()
            x, y = divmod(curr, 5)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                ni = nx * 5 + ny
                # and로 if 조건문 전부 묶기
                if 0 <= nx < 5 and 0 <= ny < 5 and ni in selected and ni not in seen:
                    seen.add(ni)
                    queue.append(ni)
                    connected += 1
                    if girls_class[nx][ny] == 'S':
                        s_count += 1
        return connected == 7 and s_count >= 4

    def seven_princess(start, depth, y_count, selected):
        global ans
        if y_count >= 4:
            return
        
        if depth == 7:
            if is_valid(selected):
                ans += 1
            return
        
        for i in range(start, 25):
            selected.add(i)
            x, y = divmod(i, 5)
            # 기본 y_count에 girls_class[x][y]가 'Y'이면 1 추가
            seven_princess(i + 1, depth + 1, y_count + (girls_class[x][y] == 'Y'), selected)
            selected.remove(i)
    seven_princess(0, 0, 0, set())
    print(ans)
