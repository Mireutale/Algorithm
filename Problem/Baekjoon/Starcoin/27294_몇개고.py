"""
* Codes\starcoin\25904_안녕클레오파트라.py
* Author : mireutale


TODO 
[설계]
T 시간 (0 ~ 23), S 술의 유무 (0 ~ 1)
T가 11이하이면 아침시간, 12에서 16이하이면 점심시간, 17이상이면 저녁시간
S가 1이면 술과 함께, 0이면 술 없이 먹는 것을 의미

밥알이 320인지 280개인지 정하라
"""
#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    t, s = map(int, input().split())
    # 술을 마시는지 아닌지
    if s == 1:
        print(280)
    else:
        # 점심시간
        if 12 <= t and t <= 16:
            print(320)
        else:
            print(280)