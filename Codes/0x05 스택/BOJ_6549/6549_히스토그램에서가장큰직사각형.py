#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
히스토그램 : 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형
직사각형은 같은 너비를 가지지만, 높이는 다름
히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램

스택에 현재 값과 index를 같이 저장
다음에 오는 값이 stack에 저장되어 있는 값과 비교했을 때 크기가 작으면 직사각형을 stack에 저장된 높이만큼
오른쪽으로 늘릴수 없음.
따라서 현재까지 저장한 값을 기준으로 크기를 재야 함.

현재 값이 더 작은 경우
stack에 있는 값을 pop하고, 가능한 직사각형의 크기를 재서 max보다 크면 max값을 변경

가능한 직사각형 크기 -> 현재 index에서 stack에 저장된 인덱스를 빼면 크기를 구할 수 있음.
"""

if __name__ == "__main__":
    while True:
        # height[0] = N, height[1:] = 직사각형들의 높이
        input_data: list = list(map(int, input().split()))
        N = input_data[0]
        heights = input_data[1:]
        if N == 0:
            break
        
        if heights:
            stack: list = []
            max_area: int = 0
            
            # 입력된 직사각형의 높이를 전부 확인하면서 stack에 넣는 작업
            for i in range(0, N):
                new_data = heights[i]
                # 현재 값이 더 작거나 같은 경우
                while stack and stack[-1][0] > new_data:
                    max_area = max(max_area, stack[-1][0] * (i - stack[-1][1]))
                    stack.pop()

                # 그 외의 경우에는 stack에 값 입력
                stack.append([new_data, i])
            
            # stack에 더 넣을 직사각형이 없으므로, 가장 마지막 직사각형의 너비도 추가해서 계산해야 하기 때문에 i에 1을 추가
            i += 1

            #더 이상 넣을 직사각형이 없는 경우, stack을 전부 비울때 까지 직사각형의 넓이를 계산
            while stack:
                max_area = max(max_area, stack[-1][0] * (i - stack[-1][1]))
                stack.pop()

        print(max_area)