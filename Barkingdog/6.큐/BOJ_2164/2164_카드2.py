"""
* CodingTest/Barkingdog/6.큐/BOJ_2164/2164_카드2.py
* Author : mireutale
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

N장의 카드가 순서대로 놓여있다.
1번이 가장 위, N번 카드가 제일 아래인 상태

카드가 한장 남을 때 까지, 제일 위에있는 카드를 바닥에 버리고
제일 위에있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

마지막으로 남게되는 카드를 구하기.

큐는 FIFO이므로, pop을 한 데이터가 제일 위에있는 카드
append를 한 데이터가 제일 아래에 있는 카드 밑으로 이동하게 된다.
"""

if __name__ == "__main__":
    n = int(input())
    queue = deque(i+1 for i in range(n))
    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue.pop())
    