# Barkingdog/17.그리디/BOJ_2457/2457_공주님의정원.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    flowers_number = int(input())
    flower_list = deque()
    for _ in range(flowers_number):
        # * 피는 월, 피는 일, 지는 월, 지는 일
        start_month, start_day, last_month, last_day = map(int, input().split())
        # ? x월 y일인 경우, xy의 형태로 저장 -> 3월 1일 = 301
        flower_list.append([start_month*100 + start_day, last_month*100 + last_day])
    # * 첫번째 원소는 오름차순, 첫번째 원소가 같은 경우, 두번째 원소 기준으로는 내림차순
    # ? 꽃이 피는 일을 기준으로는 오름차순, 지는 일을 기준으로는 내림차순
    # ? 똑같은 날에 피고, 더 빨리지는 꽃은 필요가 없음
    flower_list = deque(sorted(flower_list, key=lambda x: (x[0], -x[1])))
    
    start = 301
    flowers_count = 0
    temp_dict = {}
    
    while flower_list:
        # ? 개화, 낙화
        flowering, wither = flower_list.popleft()
        
        if start <= 1130:
            # 현재 시작일보다 개화시기가 전이라면
            if flowering <= start:
                # 같은 시작일이 있으면 더 큰 wither 값으로 업데이트
                if flowering not in temp_dict:
                    temp_dict[flowering] = wither
            # 현재 시작일보다 개화시기가 후 라면
            else:
                # 현재까지 저장된 꽃들 중 가장 늦게 지는 꽃 선택
                if temp_dict:
                    max_wither = max(temp_dict.values())
                    start = max_wither
                    flowers_count += 1
                    temp_dict.clear()
                    # 오늘을 기준으로, 가장 늦게 지는 꽃 설정
                    temp_dict[flowering] = wither
    
    # 마지막으로 남은 꽃들 처리
    if start <= 1130:
        if start >= flowering:
            if temp_dict:
                max_wither = max(temp_dict.values())
                start = max_wither
                flowers_count += 1
    
    if start > 1130:
        print(flowers_count)
    else:
        print(0)