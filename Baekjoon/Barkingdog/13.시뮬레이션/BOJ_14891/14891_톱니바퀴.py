# Barkingdog/13.시뮬레이션/BOJ_14891/14891_톱니바퀴.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def rotate(rotate_gear, rotate_direction):
    gear_idx = rotate_gear - 1
    
    # 각 톱니바퀴의 회전 여부를 저장할 리스트
    rotate_list = [False] * 4
    rotate_list[gear_idx] = True
    
    # 회전 방향을 저장할 리스트 (1: 시계, -1: 반시계)
    direction_list = [0] * 4
    direction_list[gear_idx] = rotate_direction
    
    # 왼쪽 톱니바퀴들 확인
    for i in range(gear_idx, 0, -1):
        if gear_list[i][6] != gear_list[i-1][2]:
            rotate_list[i-1] = True
            direction_list[i-1] = -direction_list[i]
        else:
            break
    
    # 오른쪽 톱니바퀴들 확인
    for i in range(gear_idx, 3):
        if gear_list[i][2] != gear_list[i+1][6]:
            rotate_list[i+1] = True
            direction_list[i+1] = -direction_list[i]
        else:
            break
    
    # 회전 실행
    for i in range(4):
        if rotate_list[i]:
            if direction_list[i] == 1:  # 시계 방향
                gear_list[i].rotate(1)
            else:  # 반시계 방향
                gear_list[i].rotate(-1)

if __name__ == "__main__":
    # 1, 2, 3, 4번 톱니바퀴의 상태를 입력받음
    gear_list = deque()
    for _ in range(4):
        gear = deque(map(int, input()))
        gear_list.append(gear)

    # 회전 횟수를 입력받음
    k = int(input())
    for _ in range(k):
        rotate_gear, rotate_direction = map(int, input().split())
        rotate(rotate_gear, rotate_direction)

    count = 0
    for i in range(4):
        count += gear_list[i][0] * (2**i)
    print(count)
