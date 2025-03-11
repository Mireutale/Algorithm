#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
0
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

"""

if __name__ == "__main__":
    N = int(input())
    stack = []
    count = 0
    for i in range(N):
        new_data = int(input())
        while stack and stack[-1][0] < new_data:
            stack.pop()
        
        stack.append([new_data, 1])
    print(count)