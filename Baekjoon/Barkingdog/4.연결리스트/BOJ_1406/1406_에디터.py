# Barkingdog/4.연결리스트/BOJ_1406/1406_에디터.py

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
영어 소문자만을 기록, 최대 600,000글자

커서는 문장의 맨 앞(첫번째 문자의 왼쪽)
문장의 맨 뒤(마지막 문자의 오른쪽)
문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있음.

길이가 L인 문자열이 현재 편집기에 입력 -> L+1가지 위치에 커서가 위치 가능

커서는 기본적으로 문장의 맨 뒤에 위치

명령어
L : 커서를 왼쪽으로 한칸(문장의 맨 앞이면 무시)
D : 커서를 오른쪽으로 한 칸 옮김(커서가 문장의 맨 뒤면 무시)
B : 커서 왼쪽에 있는 문자를 삭제(커서가 문장의 맨 앞이면 무시)
P $ : $라는 문자를 커서 왼쪽에 추가함.

! 시간 초과 문제 발생 -> insert를 deque에서 수행하면 시간이 오래 걸림
! O(n)의 시간을 줄이기 위해서 커서의 왼쪽과 오른쪽 문자열로 변경
"""
if __name__ == "__main__":
    # 커서는 left_stack의 끝 문자 바로 뒤에 존재
    left_stack = list(input().rstrip())  # 커서 왼쪽 문자들
    right_stack = []  # 커서 오른쪽 문자들
    nums_of_commands = int(input())

    for _ in range(nums_of_commands):
        command = input().split()
        if command[0] == "L":
            # 커서가 문자의 가장 앞에 있지 않은 경우
            if left_stack:
                # left의 가장 뒤에 있는 문자를 right에 입력
                right_stack.append(left_stack.pop())
        elif command[0] == "D":
            # 커서가 문자의 가장 뒤에 있지 않은 경우
            if right_stack:
                # right의 가장 뒤에 있는 문자 == cursor바로 뒤에 있는 문자를 left로 이동
                left_stack.append(right_stack.pop())
        elif command[0] == "B":
            # 커서의 왼쪽 문자를 제거
            if left_stack:
                left_stack.pop()
        elif command[0] == "P":
            # 커서의 왼쪽에 원하는 문자를 추가
            left_stack.append(command[1])

    # 결과 출력
    # 왼쪽 stack은 그대로, 오른쪽 스택은 역방향으로 더한다.
    print(''.join(left_stack + right_stack[::-1]))
