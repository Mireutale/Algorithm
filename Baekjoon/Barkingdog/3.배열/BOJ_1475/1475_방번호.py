# Barkingdog/3.배열/BOJ_1475/1475_방번호.py

import sys
import math
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

6과 9는 뒤집어서 사용 가능하고, 한 세트에 0 ~ 9번까지의 숫자가 들어있다.
방 번호가 주어진 경우 필요한 세트의 최솟값을 구하는 문제

입력된 방 번호에 따라서 필요한 숫자의 개수를 파악 -> 세트의 개수를 계산
"""

if __name__ == "__main__":
    room_number = input()
    #! 6과 9는 동일한 수로 계산
    need_number = [0] * 9
    for i in range(len(room_number)):
        if room_number[i] == "9":
            need_number[6] += 1
        else:
            need_number[int(room_number[i])] += 1
    need_number[6] /= 2
    print(math.ceil(max(need_number)))
