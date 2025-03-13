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

가능한 직사각형 크기 -> stack의 블럭 높이 * index - 1 - (스택의 마지막 값의 인덱스)
"""

if __name__ == "__main__":
    while True:
        # height[0] = N, height[1:] = 직사각형들의 높이
        input_data: list = list(map(int, input().split()))
        # 0이 입력되서 종료
        if input_data[0] == 0:
            break
        
        stack = []
        n: int = input_data[0]
        max_area: int = 0
        for i in range(1, n+1):
            if len(stack) == 0:
                stack.append([input_data[i], i])
            else:
                # 스택의 값보다 현재 값이 더 큰 경우 -> 그대로 입력
                if stack[-1][0] <= input_data[i]:
                    stack.append([input_data[i], i])
                # 현재 값이 스택의 값보다 더 작은 경우
                else:
                    while stack and stack[-1][0] > input_data[i]:
                        top = stack.pop()[0]
                        # 현재 값 보다, 더 낮은 높이의 block이 있었던 경우
                        if stack:                        
                            width = i - (stack[-1][1]) -1
                        # 현재 값이 가장 낮은 높이의 block 인 경우
                        else:
                            width = i - 1
                        max_area = max(max_area, top * width)
                    stack.append([input_data[i], i])
            
        # 모든 input값을 확인하고 남은 stack에 있는 값들에서 area를 계산
        while stack:
            top = stack.pop()[0]
            if len(stack) == 0:
                width = n
            else:
                width = n - stack[-1][1]
            max_area = max(max_area, top * width)
        print(max_area)