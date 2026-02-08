# Barkingdog/13.시뮬레이션/BOJ_11559/11559_Puyo Puyo.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, w, l = map(int, input().split())
    waiting_trucks = deque(map(int, input().split()))
    bridge = deque([0] * w)
    unit_time = 0
    weight_on_bridge = 0
    while bridge:
        unit_time += 1
        weight_on_bridge -= bridge.popleft() # 한칸 앞으로 이동

        if waiting_trucks: # 가야할 트럭 있음
            if weight_on_bridge + waiting_trucks[0] <= l: # 무게를 버틸 수 있다면
                truck = waiting_trucks.popleft() # 다리위에 올라갈 트럭
                bridge.append(truck) # 다리위에 추가
                weight_on_bridge += truck # 무게 계산
            else:
                bridge.append(0)
    
    print(unit_time)
