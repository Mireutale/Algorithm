"""
* CodingTest/Barkingdog/5.스택/BOJ_17298/17298_오큰수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
크기 N인 수열의 각 원소 Ai에 대해서 오큰수를 구한다.
오큰수는 오른쪽에 있으면서, Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
오큰수가 없는 경우, -1

N, Ai (1 ~ 1,000,000) / 시간제한 1초, 메모리 512MB

시간제한 1초 -> 이중 for문 사용 불가.

뒤에서부터 확인하면서, stack에 값 추가
현재 값보다 stack에 있는 값이 작으면 pop 수행
stack에 있는 값 확인해서 ans에 결과를 추가
"""

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    mono_stack = []
    ans = []
    for i in range(N-1, -1, -1):
        while mono_stack and mono_stack[-1] <= data[i]:
            mono_stack.pop()
        if mono_stack:
            ans.append(mono_stack[-1])
        else:
            ans.append(-1)
        mono_stack.append(data[i])
    print(' '.join(map(str, ans[::-1])))