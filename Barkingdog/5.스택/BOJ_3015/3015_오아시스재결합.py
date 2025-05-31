"""
* Barkingdog\0x05 스택\BOJ_3015\3015_오아시스재결합.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

#! 이 경우 모든 수가 같은 경우이면 -> 시간 복잡도가 O(n^2)
for j in range(len(stack)-1, -1, -1):
    if stack[j] > new_data:
        count += 1
        break
    else:
        count += 1

위 count를 더 낮은 복잡도로 수행해야 풀 수 있다..

stack에 값을 [num_data, num_count]로 넣어서 문제 풀기
"""

if __name__ == "__main__":
    N = int(input())
    stack = []
    count = 0
    for i in range(N):
        new_data = int(input())

        # 기존 스택의 값이 현재보다 작은 경우
        while stack and stack[-1][0] < new_data:
            count += stack.pop()[1]

        # 기존에 스택이 비어있거나, 스택의 마지막 값(이전 가장 작은 값)이 현재 데이터 보다 큰 경우
        # 스택에는 계속에서 값을 추가해야 하고, 결과는 +1
        if not stack:
            stack.append([new_data, 1])

        # 기존에 스택의 값이 현재와 같은 경우
        elif stack and stack[-1][0] == new_data:
            # 스택에 지금 값이 같은 값과 다른 값도 들어있다면?
            # 현재와 같은 값은 전부 볼 수 있고, 이보다 큰 값은 가장 앞에있는 1개만 볼 수 있음
            if stack[0][0] != stack[-1][0]:
                count += stack[-1][1] + 1
                stack[-1][1] += 1

            # 스택에 현재와 동일한 값만 들어있는 경우
            if stack[0] == stack[-1]:
                count += stack[-1][1]
                stack[-1][1] += 1
        
        elif stack[-1][0] > new_data:
            stack.append([new_data, 1])
            count += 1

    print(count)