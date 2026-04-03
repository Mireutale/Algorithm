# Barkingdog/14. 정렬 I/BOJ_15688/15688_수 정렬하기 5.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    # sort활용
    # nums.sort(reverse=True)
    # for num in nums:
    #     print(num)

    # sorted활용
    # for num in reversed(sorted(nums)):
    #     print(num)

    # 직접 구현
    def arr_sort(arr):
        pass