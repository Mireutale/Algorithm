# Barkingdog/14. 정렬 I/BOJ_2750/2750_수 정렬하기.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    
    # sort 활용
    # arr.sort()
    # for num in arr:
    #     print(num)

    # ? # arr.sort(reverse = True), 내림차순 정렬
    
    # sorted 활용
    # for num in sorted(arr):
    #     print(num)

    # ? arr = sorted(arr, reverse = True), 내림차순 정렬

    # 직접 구현
    def arr_sort(arr):
        pass