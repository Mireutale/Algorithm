"""
* Barkingdog\0x09 BFS\BOJ_9466\9466_텀프로젝트.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
# 사이클의 (재귀)순환 제한수를 늘림
sys.setrecursionlimit(10**6)

def dfs(i):
    # 전역변수의 값을 변화하기 위해서 사용
    global team_student_count

    visited[i] = True # 방문
    team.append(i) # 팀에 추가
    choose = student_choose_list[i] # 현재 학생이 선택한 학생

    if visited[choose]: # 이미 방문한 학생이고
        if choose in team: # 팀 후보에 있는 경우
            team_student_count += len(team[team.index(choose):])
    else: # 처음 방문한 학생
        dfs(choose)

if __name__ == "__main__":
    testcase_num = int(input())
    for _ in range(testcase_num):
        all_student_numbers = int(input())
        student_choose_list = [0] + list(map(int, input().split()))
        visited = [False] * (all_student_numbers + 1)
        team_student_count = 0

        for i in range(1, all_student_numbers+1):
            if not visited[i]:
                team = []
                dfs(i)
        print(all_student_numbers - team_student_count)