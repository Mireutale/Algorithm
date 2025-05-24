"""
* Barkingdog\0x06 큐\BOJ_10845\10845\10845_큐1_18258_큐2.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
queue는 선입선출(FIFO) 기반의 자료구조로, 먼저 넣은 자료가 먼저 나오는 형태이다.

collections 라이브러리의 deque는 스택과 큐의 기능을 모두 가진 객체로
출입구를 양쪽에 가지는 형태의 객체이므로, 이 객체를 큐 처럼 사용하기로 하였다.

deque사용법
    오른쪽 append / pop
    왼쪽 appendleft / popleft


큐를 구현하고 명령을 처리하는 프로그램을 작성하는 문제
push X : 정수 X를 큐에 넣는 연산
pop : 큐에서 가장 앞에 있는 정수를 빼고, 수를 출력 / 큐가 비어있으면 -1 출력
size : 큐에 들어있는 정수의 개수 출력
empty : 큐가 비어있으면 1, 아니면 0을 출력한다.
front : 큐의 가장 앞에 있는 정수를 출력 / 비어있으면 -1 출력
back : 큐의 가장 뒤에 있는 정수를 출력 . 비어있으면 -1 출력
"""

if __name__ == "__main__":
    n = int(input())
    queue = deque()
    for _ in range(n):
        command = input().split()
        if command[0] == "push":
            queue.append(command[1])
        if command[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        if command[0] == "size":
            print(len(queue))
        if command[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        if command[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        if command[0] == "back":
            if queue:
                print(queue[-1]) 
            else:
                print(-1)