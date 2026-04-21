"""
* Codes\starcoin\25904_안녕클레오파트라.py
* Author : mireutale


TODO 
[설계]
게임 참여 인원 N, 1번이 처음으로 낼 목소리의 높이 X (3 ~ N ~ 100, 1 ~ X ~ 100)

N개의 정수 t1, t2, ..., tn이 공백으로 구분되어 주어짐
ti -> i번이 낼 수 있는 목소리 높이의 상한선 (1 ~ ti ~ 200)

더 이상 목소리를 내지 못해 지는 경우에 걸린 사람의 번호 출력
"""

#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, x = map(int, input().split())
    max_sound = list(map(int, input().split()))
    order = 0
    # 최대 높이인 200까지 반복
    for i in range(x, 200 + 1):
        # 수행해야 하는 사람의 번호
        people_order =  order % n
        order += 1
        # i는 현재 내야하는 목소리의 높이
        if i > max_sound[people_order]:
            print(people_order + 1)
            exit()