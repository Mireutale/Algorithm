#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

키로거 : 사용자가 키보드를 누른 명령을 모두 기록한다.

비밀번호 창에서 입력한 키가 주어진 경우, 비밀번호를 알아내는 프로그램

키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스['-'], 화살표['<', '>']
"""

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        left_stack = []
        right_stack = []
        commands = input()
        for command in commands:
            # 화살표 왼쪽
            if command == "<":
                if left_stack:
                    right_stack.append(left_stack.pop())
            # 화살표 오른쪽
            elif command == ">":
                if right_stack:
                    left_stack.append(right_stack.pop())
            # 백스페이스
            elif command == "-":
                if left_stack:
                    left_stack.pop()
            else:
                left_stack.append(command)
        print(''.join(left_stack + right_stack[::-1]))