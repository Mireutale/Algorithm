#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]
첫 줄 F S G U D (1 ~ S, G ~ F, 1,000,000) / (0 ~ U, D ~ 1,000,000)

건물은 1층부터 시작, 가장 높은 층은 F층

현재 위치는 S층, 스타트링크가 있는 곳은 G층

U는 위로 U층, D는 아래로 D층 이동 하는 버튼

G층에 도착하려면 최소한 버튼을 몇 번 눌러야하는지 구하기, 엘리베이터를 이용해 갈 수 없다면 "user the stairs" 출력
"""
if __name__ == "__main__":
    F, S, G, U, D = map(int, input().split())
    visited = [False] * (F + 1) # F층까지 방문 여부 확인
    queue = deque()
    queue.append((S, 0)) # 현재 층, 버튼 누른 횟수
    visited[S] = True # 현재 층 방문 처리
    move = [U, -D]
    can_go_S = False
    while queue:
        now, count = queue.popleft()
        if now == G:
            print(count)
            can_go_S = True
            break
        for i in range(2):
            new_now = now + move[i]
            if 0 < new_now <= F and not visited[new_now]:
                queue.append((new_now, count + 1))
                visited[new_now] = True
    if not can_go_S:
        print("use the stairs")