#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
N개의 원소를 포함하고 있는 양방향 순환 큐를 가진다.
이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

1. 첫번째 원소 뽑아내기
2. 왼쪽으로 한칸 이동시키기
3. 오른쪽으로 한칸 이동시키기

원하는 연산을 수행하기 위해 해야하는 2,3번 연산의 최솟값을 출력

N (1 ~ 50) / M (1 ~ N)

추가로 생각한 풀이..
덱에 [1, N]을 넣고, 쪼갤때 마다 left right를 계산하고, left값이 더 크면 또 쪼개기...
-> 구현이 너무 복잡

deque의 index 함수와, rotate를 잘 사용하자
"""

if __name__ == "__main__":
    N, M = map(int, input().split())
    pop_out = map(int, input().split())
    # 첫번째 원소 뽑아내기만 가능하므로, 반드시 뽑으려는 원소를
    # 처음으로 이동시켜야 함.
    # 왼쪽 or 오른쪽 중 더 가까운 쪽으로 이동 연산을 수행
    count = 0
    deck = deque(i for i in range(1, N+1))
    for pop_int in pop_out:
        while True:
            if pop_int == deck[0]:
                deck.popleft()
                break
            else:  
                # 원하는 원소의 위치가 중간 값 보다 작은 경우
                # 왼쪽 이동이 유리
                if deck.index(pop_int) <= len(deck) / 2:
                    deck.rotate(-1)
                    count += 1
                # 반대의 경우 오른쪽 이동이 유리
                else:
                    deck.rotate(1)
                    count += 1
    print(count)