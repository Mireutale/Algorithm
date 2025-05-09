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

def move_robots(belt_durability, robot_position, belt_range, belt_durability_count_zero):
    # 로봇 걷기
    for i in range(len(robot_position)):
        if robot_position[i] == 1:
            if i + 1 == len(robot_position):
                robot_position[i] = 0
            else:
                if belt_durability[i+1] != 0:
                    robot_position[i], robot_position[i+1] = robot_position[i+1], robot_position[i]
                    belt_durability[i+1] -= 1
                    if belt_durability[i+1] == 0:
                        belt_durability_count_zero += 1
    return belt_durability_count_zero


def load_robot(belt_durability, robot_position, belt_durability_count_zero):
    # 로봇 올리기
    if belt_durability[0] > 0:
        if robot_position[0] == 0:
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
        print("after rotate", belt_durability)

        # 로봇 걷기
        print("robot position", robot_position)
        belt_durability_count_zero = move_robots(
            belt_durability, robot_position, belt_range, belt_durability_count_zero
        )
        print("after walk", belt_durability)
        if zero_durability_count <= belt_durability_count_zero:
            print(answer)
            exit()

        # 로봇 올리기
        belt_durability_count_zero = load_robot(belt_durability, robot_position, belt_durability_count_zero)
        print("after load", belt_durability)
    print(answer)

# commit msg
# --- 문제풀이_mireutale[25/ / ]