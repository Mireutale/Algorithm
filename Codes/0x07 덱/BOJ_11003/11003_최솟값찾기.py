#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

N개의 수 A1,A2, ... , AN과 L(1 ~ L ~ N ~ 5,000,000)이 주어진다.

Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는
프로그램

이때 i <= 0인 Ai는 무시하고 D를 구해야 함.
"""

if __name__ == "__main__":
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    # 덱에 [data, index] 형태로 값을 저장하고, 최솟값을 가장 왼쪽에 두기.
    deck = deque()
    ans = []
    for i in range(N):
        if i-L+1 < 0:
            temp = 0
        else:
            temp = i-L+1
        # !min을 사용하면 최솟값을 찾는데 시간이 오래 걸림.
        # ans.append(min(A[temp:i+1]))
    print(' '.join(map(str, ans)))