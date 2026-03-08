# Barkingdog/14. 정렬 I/BOJ_2750/2750_수 정렬하기.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    
    # sort
    # arr.sort()
    # arr.sort(reverse = True)
    # for num in arr:
    #     print(num)
    
    # sorted
    # arr = sorted(arr, reverse = True)
    # for num in sorted(arr):
    #     print(num)

    # 구현
    def arr_sort(arr):
        pass