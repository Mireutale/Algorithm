# PG 49994 방문 길이

import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(dirs):
    # x, y, dir으로 이루어진 3차원 배열
    visited = [[[0] * 4 for _ in range(11)] for _ in range(11)]
    answer = 0
    x, y = 0, 0
    UDRL = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    for dir in dirs:
        dx, dy = UDRL[dir]
        nx, ny = x + dx, y + dy

        # 방향 숫자로 지정
        if dir == "U":
            dirp = 0
            other_dirp = 1
        elif dir == "D":
            dirp = 1
            other_dirp = 0
        elif dir == "R":
            dirp = 2
            other_dirp = 3
        else:
            dirp = 3
            other_dirp = 2

        # 경계를 벗어나지 않으면 이동
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 이동하지 않은 경로
            if not visited[x + 5][y + 5][dirp]:
                visited[x + 5][y + 5][dirp] = 1
                visited[nx + 5][ny + 5][other_dirp] = 1
                answer += 1
            x, y = nx, ny
    return answer

if __name__ == "__main__":
    dirs = input()
    print(solution(dirs))