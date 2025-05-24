"""
* Barkingdog\0x05 스택\BOJ_2493\2493_탑.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

탑의 수를 나타내는 정수 n (1 ~ 500,000)
n개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고
주어짐. 탑의 높이 정수(1 ~ 100,000,000)

탑은 왼쪽 방향으로 수평 직선으로 레이저 신호를 보내고, 가장 먼저
만나는 탑에서만 수신이 가능하다.

주어진 순서대로 왼쪽부터 오른쪽 방향으로 탑을 세움

이중 for문 사용시 시간 초과 -> 스택에 현재 타워의 높이보다 큰 타워의 인덱스만 저장하면 해결
모든 값 확인 안해도 됨.
! 문제코드
if __name__ == "__main__":
    n = int(input())
    tower = input().split()
    ans = []
    while tower:
        data = tower.pop()
        ! 현재 타워보다 큰 타워를 찾기 위해서 계속해서 반복을 수행 -> 시간이 오래걸림
        for i in range(len(tower)-1, -1, -1):
            if tower[i] >= data:
                ans.append(i+1)
                break
            if i == 0:
                ans.append(0)
    ans.append(0)
    print(" ".join(map(str, ans[::-1])))
"""

if __name__ == "__main__":
    n = int(input())
    towers = list(map(int, input().split()))
    stack = []
    ans = [0] * n
    for i in range(n):
        #? 만약 stack에 값이 있는데, 현재 타워의 높이보다 낮으면 stack에서 제거
        #? pop을 해도 되는 이유는? 스택의 마지막 타워가 현재 타워보다 높이가 낮음
        #? 다음 타워(i+1)는 현재 타워(i)를 더 먼저 만나기 때문에, 현재 타워보다 높이가 낮은 stack에 있는 타워를 유지할 이유 없음.
        while stack and stack[-1][0] < towers[i]:
            stack.pop()
        #? stack에 값이 있는경우, 현재 타워의 높이보다 높은 값이 남아있으므로, stack에 가장 마지막 타워가 레이저를 수신
        #? 수신한 타워의 번호를 ans에 추가
        if stack:
            ans[i] = stack[-1][1] + 1
        #? 다음 타워는 지금 타워의 높이도 확인해야함 -> stack에 값 추가
        stack.append((towers[i], i))
    print(" ".join(map(str, ans)))


# # 더 빠른 해결법
# n = int(input())
# # ! 타워를 거꾸로 저장
# towers = map(int, reversed(input().split()))
# stack = []
# ans = [0]*n
# # ! enumerate를 사용해서 인덱스와 높이를 할당
# for idx, height in enumerate(towers):
#     # ? 스택이 있는 경우
#     if stack and stack[-1][1] < height:
#         # ? 현재 타워의 높이가 스택에 할당된 타워보다 큰 경우 -> 현재 타워가 스택에 있는 타워의
#         # ? 레이저를 수신하기 때문에, ans에 값을 입력
#         while stack and stack[-1][1] < height:
#             ans[stack[-1][0]] = n - idx
#             print(ans)
#             stack.pop()
#     # ? 현재 타워를 스택에 입력, 타워를 거꾸로 저장했으므로, n-idx-1을 사용
#     stack.append((n - idx - 1, height))