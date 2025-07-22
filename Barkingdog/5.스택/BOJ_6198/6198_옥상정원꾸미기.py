"""
* CodingTest/Barkingdog/5.스택/BOJ_6198/6198_옥상정원꾸미기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

N개의 빌딩, i번째 빌딩의 키가 hi 모든 빌딩은 일렬로 서 있고
오른쪽으로만 볼 수 있다.

i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1, i+2, ... , N이다.
그러나, 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음 빌딩의 옥상은 보지 못함.

첫 번째 줄에 빌딩의 개수 N (1 ~ 80,000)
두 번째 줄 부터 각 빌딩의 높이 (1 ~ 1,000,000,000)이 입력된다.

시간제한 1초 -> for문 사용 x

생각한 풀이
스택을 활용 O(1)으로 값을 추가하거나 제거해서 문제 풀기

스택에는 현재 건물을 볼 수 있는 건물만 남기자.
"""

if __name__ == "__main__":
    N = int(input())
    building = [int(input()) for _ in range(N)]
    can_see_this_building = []
    count = 0
    #? h는 현재 건물
    for h in building:
        # 현재 건물을 볼 수 있는 건물이라고 생각되는 건물 중
        # 현재 건물보다 높이가 낮은 건물 -> 현재 건물의 옥상정원을 볼 수 없음
        # 따라서 스택에서 제외
        while can_see_this_building and can_see_this_building[-1] <= h:
            can_see_this_building.pop()
        # 현재 건물을 볼 수 있는 건물 -> 현재 건물보다 높고 왼쪽에 있는 건물
        count += len(can_see_this_building)
        can_see_this_building.append(h)
    print(count)