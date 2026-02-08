# Barkingdog/3.배열/BOJ_3273/3273_두수의합.py

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
n개의 서로 다른 양의 정수로 이루어진 수열 -> 중복되는 값이 없음
ai의 값은 1 ~ 1000000 사이의 자연수
자연수 x가 주어진 경우에서 ai + aj = x를 만족하는 (ai, aj)쌍의 수를 구하는 프로그램 작성

문제점1
#! 인덱스를 정방향으로 순회하면서 pop을 사용하면 indexerror가 발생할 가능성 있음
# for i in range(n):
#     if numbers[i] >= x:
#         numbers.pop(i)
#? 해결방법 -> 리스트 컴프리헨션을 사용해서 문제 해결
numbers = [num for num in numbers if num < x]

문제점2
시간 초과가 발생 -> 이중 for문 활용시 모든 가능성을 다 확인하므로 너무 느림
정렬 후 left와 right를 사용한 투 포인터를 활용
"""

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    x = int(input())
    #? 중복되는 값이 없으므로 set을 사용해도 문제 해결 가능
    numbers = sorted([num for num in numbers if num < x])
    count = 0
    left = 0
    right = len(numbers) - 1
    while left < right:
        finds = numbers[left] + numbers[right]
        #! 조합을 찾은 경우
        if finds == x:
            count += 1
            left += 1
            right -= 1
        #! 현재 조합이 x보다 작은 경우, 조합의 결과를 더 크게 만들어야 함
        if finds < x:
            left += 1
        #! 현재 조합이 x보다 큰 경우, 조합의 결과를 더 작게 만들어야 함
        if finds > x:
            right -= 1
    print(count)
