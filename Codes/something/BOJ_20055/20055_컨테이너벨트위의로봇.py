"""
* Codes\something\BOJ_20055\20055_컨테이너벨트위의로봇.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def rotate_belt(belt_durability, robot_position):
    # 벨트 및 로봇 회전
    belt_durability.rotate(1)
    robot_position.rotate(1)
    robot_position[belt_range-1] = 0

def move_robots(belt_durability, robot_position, belt_range, belt_durability_count_zero):
    # 로봇 걷기
    for i in range(len(robot_position) -2, -1, -1):
        # 로봇이 벨트 위에 있는 경우
        if robot_position[i] == 1:
            if robot_position[i+1] == 0 and belt_durability[i+1] > 0:
                robot_position[i] = 0
                robot_position[i+1] = 1
                belt_durability[i+1] -= 1
                if belt_durability[i+1] == 0:
                    belt_durability_count_zero += 1
    # 로봇이 내리는 위치에 있는 경우
    robot_position[belt_range-1] = 0
    return belt_durability_count_zero


def load_robot(belt_durability, robot_position, belt_durability_count_zero):
    # 로봇 올리기
    if belt_durability[0] > 0 and robot_position[0] == 0:
        robot_position[0] = 1
        belt_durability[0] -= 1
        if belt_durability[0] == 0:
            belt_durability_count_zero += 1
    return belt_durability_count_zero

if __name__ == "__main__":
    belt_range, zero_durability_count = map(int, input().split())
    belt_durability = deque(list(map(int, input().split())))
    robot_position = deque(list([0]*(belt_range)))
    belt_durability_count_zero = 0
    answer = 0
    while zero_durability_count > belt_durability_count_zero:
        answer += 1
        # 벨트 회전
        rotate_belt(belt_durability, robot_position)
        # print("after rotate", belt_durability, robot_position)

        # 로봇 걷기
        belt_durability_count_zero = move_robots(
            belt_durability, robot_position, belt_range, belt_durability_count_zero
        )
        # print("after walk", belt_durability, robot_position)
        if zero_durability_count <= belt_durability_count_zero:
            print(answer)
            exit()

        # 로봇 올리기
        belt_durability_count_zero = load_robot(belt_durability, robot_position, belt_durability_count_zero)
        #print("after load", belt_durability, robot_position, answer)
    print(answer)