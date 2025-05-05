"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale
"""


import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    testcase_num = int(input())
    for _ in range(testcase_num):
        all_student_numbers = int(input())
        student_choose_list = list(map(int, input().split()))
        team_student = [False] * (all_student_numbers + 1)
        team_student_count = 0
        queue = deque()
        for i in range(all_student_numbers):
            student = i + 1
            student_choose = student_choose_list[student-1]
            queue.append([student, student_choose])
            select_list = deque()
            while queue:
                num, choose = queue.popleft()
                select_list.append(num)
                if not team_student[num]:
                    if num != choose:
                        if choose not in select_list:
                            queue.append([choose, student_choose_list[choose-1]])
                        else:
                            while select_list:
                                team_student[select_list.pop()] = True
                                team_student_count += 1
                    if num == choose:
                        if num == select_list[0]:
                            while select_list:
                                team_student[select_list.pop()] = True
                                team_student_count += 1
        print(all_student_numbers - team_student_count)

# commit msg
# --- 문제풀이_mireutale[25/ / ]