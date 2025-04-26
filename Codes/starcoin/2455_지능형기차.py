#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
1~4의 기차역 -> 출발역에서 종착역까지 가는 도중 기차안에 사람이 가장 많을 때의 사람 수 계산

각 역에서 내린 사람 수와 탄 사람 수가 주어진다.
"""

if __name__ == "__main__":
    who_in_train = 0
    max_people = 0
    for _ in range(4):
        who_got_off, who_got_in = map(int, input().split())
        who_in_train += who_got_in - who_got_off
        max_people = max(max_people, who_in_train)
    print(max_people)