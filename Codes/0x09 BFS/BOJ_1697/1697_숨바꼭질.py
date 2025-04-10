import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]

현재 점 N(0 ~ 100,000)에 수빈이가 위치, 동생은 점 K(0 ~ 100,000)에 위치
수빈이는 걷거나 순간이동을 할 수 있다.
위치가 X일 때, 걷는다면 1초 후 X - 1, X + 1로 이동 가능
순간이동을 하는 경우 1초 후 2*X의 위치로 이동 가능

동생을 찾을 수 있는 가장 빠른 시간을 출력

ex) 5 17

5 - 10 - 9 - 18 - 17
4초

! 시간초과
? 시간초과가 발생하지 않도록 데이터 접근 시간을 줄임
"""

if __name__ == "__main__":
    N, K = map(int, input().split())
    # 모든 경우의 수 체크
    next_possible = deque()
    next_possible.append(N)
    already = [0] * 100001 # 0 ~ 100,000
    # 가능한 다음 수가 없기 전까지 출력
    while next_possible:
        position = next_possible.popleft()
        if position == K:
            print(already[position])
            break
        # n에 0이 들어오는 경우, *2의 위치를 앞에 두게되면 already[0]의 값이 변하면서 이후의 값도 문제가 발생!
        for next in (position-1, position+1, position*2):
            # already[next]가 범위 보다 먼저 측정되는 경우 범위를 벗어나는 index에러가 발생할 수 있으므로 순서에 유의!
            if 0 <= next <= 100000 and already[next] == 0:
                already[next] = already[position] + 1
                next_possible.append(next)