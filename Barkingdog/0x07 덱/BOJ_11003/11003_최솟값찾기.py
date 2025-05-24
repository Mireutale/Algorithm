"""
* Barkingdog\0x07 덱\BOJ_11003\11003_최솟값찾기.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

N개의 수 A1,A2, ... , AN과 L(1 ~ L ~ N ~ 5,000,000)이 주어진다.

Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는
프로그램

이때 i <= 0인 Ai는 무시하고 D를 구해야 함.
# !min을 사용하면 최솟값을 찾는데 시간이 오래 걸림.
# ?ans.append(min(A[temp:i+1]))

해결방법
덱 안에는 가능한 범위의 값만 위치
덱을 오름차순으로 유지하여 덱의 첫번째 원소에 최솟값이 위치하도록 설정
덱의 범위에서 나가게 되는 값은 인덱스가 낮은 값.
새롭게 추가되는 값은 현재 덱에 들어있는 원소 중 가장 마지막으로 나가게 됨.
따라서, 인덱스가 낮은 값은 범위밖에 나갔는지 체크하고, 현재 값보다 큰
값은 현재 값 보다 먼저 범위를 벗어나게 됨으로 덱에 유지할 이유 없음.

메모리 초과
덱에는 인덱스만 유지 -> A를 사용하여 값 참조
"""

if __name__ == "__main__":
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    # 덱에 [data, index] 형태로 값을 저장하고, 덱을 오름차순으로 유지
    deck = deque()
    ans = []
    for i in range(N):
        if i-L+1 < 0:
            start = 0
        else:
            start = i-L+1

        # 범위를 벗어난 값 제거
        if deck and deck[0] < start:
            deck.popleft()

        # 현재 값보다 덱에 있는 큰 값 모두 제거
        while deck and A[deck[-1]] > A[i]:
            deck.pop()

        deck.append(i)
        # 덱이 오름차순이므로, 최솟값은 덱의 첫번째에 위치
        ans.append(A[deck[0]])
    print(' '.join(map(str, ans)))