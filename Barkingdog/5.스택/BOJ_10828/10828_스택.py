"""
* CodingTest/Barkingdog/5.스택/BOJ_10828/10828_스택.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
스택 구현
명령어
push X : 정수 X를 스택에 넣는 연산
pop : 스택에서 가장 위에있는 수를 제거하고, 그 수를 출력 / 스택이 비어있는 경우 -1 출력
size : 스택에 들어있는 정수의 개수 출력
empty : 스택이 비어있으면 1, 아니면 0을 출력
top : 스택의 가장 위에있는 정수를 출력, 스택에 들어있는 정수가 없는 경우에는 -1을 출력

"""

if __name__ == "__main__":
    N = int(input())
    stack = []
    for _ in range(N):
        command = input().split()
        if command[0] == "push":
            stack.append(command[1])
        if command[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        if command[0] == "size":
            print(len(stack))
        if command[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        if command[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)