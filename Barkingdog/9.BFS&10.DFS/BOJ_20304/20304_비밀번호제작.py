"""
* Barkingdog\0x09 BFS\BOJ_20304\20304_비밀번호제작.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
서버 관리자 계정 비밀번호 : 0이상 N이하의 정수 중 하나를 사용 가능

두 비밀번호의 안전 거리 : 이진법으로 표현한 두 비밀번호의 서로 다른 자리의 개수로 정의

ex) 3 : 0011, 8 : 1000 -> 서로 다른 자리의 개수는 3, 3과 8의 안전거리는 3

비밀번호의 안전도 : 로그인 시도에 사용된 모든 비밀번호와의 안전 거리중 최솟값

ex) 사용된 비밀번호가 3, 4인 경우 새로운 비밀번호 8에 대해 3과 8의 안전거리는 3, 4와 8의 안전거리는 2이므로 안전도는 2

해커가 비밀번호를 알아내기 까지의 시간을 늦추기 위해 현재 사용중인 관리자 계정 비밀번호가 안전도가 가장 높게끔 바꾸고 싶다.
안전도가 제일 높은 비밀번호의 안전도를 구하라.

n : 관리자 계정 비밀번호 최댓값(0 ~ n ~ 1,000,000)
m : 로그인 시도에 사용된 비밀번호의 개수(1 ~ m ~ 100,000)
p1 ... pm : 로그인 시도에 사용된 비밀번호 값(0 ~ pi ~ N)
"""

def bfs(n, used_passwords):
    safety_distance = [-1] * (n + 1)  # 각 비밀번호의 안전도를 저장하는 리스트 초기화
    queue = deque()  # BFS를 위한 큐 생성

    for pw in used_passwords:  # 사용된 비밀번호를 큐에 추가하고 안전도를 0으로 설정
        safety_distance[pw] = 0
        queue.append(pw)

    while queue:  # BFS 탐색 시작
        current = queue.popleft()  # 큐에서 현재 비밀번호를 꺼냄
        for i in range(n.bit_length()):  # i는 0부터 n을 이진수로 나타내는 데 필요한 비트 수 반환
            # i번째 비트를 전환
            next_pw = current ^ (1 << i)  # 현재 비밀번호와 i만큼 왼쪽으로 움직인 비트의 연산, 즉 i번째 비트가 1이면 0으로, 0이면 1로 변경
            if 0 <= next_pw <= n and safety_distance[next_pw] == -1:  # 유효한 비밀번호이고 아직 방문하지 않았다면
                safety_distance[next_pw] = safety_distance[current] + 1  # 안전도를 갱신, i번째 비트만 변경하였으므로
                queue.append(next_pw)  # 새로 구한 비밀번호를 큐에 추가

    return max(safety_distance)  # 최대 안전도 반환

if __name__ == "__main__":
    n = int(input())  # 관리자 계정 비밀번호 최댓값 입력
    m = int(input())  # 로그인 시도에 사용된 비밀번호 개수 입력
    used_passwords = list(map(int, input().split()))  # 사용된 비밀번호 리스트 입력
    print(bfs(n, used_passwords))  # BFS를 통해 최대 안전도 계산 및 출력