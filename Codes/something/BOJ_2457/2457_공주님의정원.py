"""
* Codes\something\BOJ_2457\2457_공주님의정원.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    flowers_number = int(input())
    flower_list = deque()
    for _ in range(flowers_number):
        # * 피는 월, 피는 일, 지는 월, 지는 일
        start_month, start_day, last_month, last_day = map(int, input().split())
        flower_list.append([start_month*100 + start_day, last_month*100 + last_day])
    # * 첫번째 원소는 오름차순, 첫번째 원소가 같은 경우, 두번째 원소 기준으로는 내림차순
    flower_list = deque(sorted(flower_list, key=lambda x: (x[0], -x[1])))
    
    start = 301
    flowers_count = 0
    temp_dict = {}
    
    while flower_list:
        flowering, wither = flower_list.popleft()
        
        if start <= 1130:
            if flowering <= start:
                # 같은 시작일이 있으면 더 큰 wither 값으로 업데이트
                if flowering in temp_dict:
                    temp_dict[flowering] = max(temp_dict[flowering], wither)
                else:
                    temp_dict[flowering] = wither
            else:
                # 현재까지 저장된 꽃들 중 가장 늦게 지는 꽃 선택
                if temp_dict:
                    max_wither = max(temp_dict.values())
                    start = max_wither
                    flowers_count += 1
                    temp_dict.clear()
                    # 현재 꽃도 처리
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