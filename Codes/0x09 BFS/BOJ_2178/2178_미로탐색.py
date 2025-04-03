#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
N * M 크기의 배열 -> 미로
1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸

(1, 1)에서 출발하여, (M, N)위치로 이동할 때, 지나야 하는 최소의 칸 수를 구하기
"""

if __name__ == "__main__":
    N, M = map(int, input().split())
    mage = list([] for _ in range(N))
    for i in range(N):
        input_line = input()
        for data in input_line:
            mage[i].append(int(data))
    print(mage)