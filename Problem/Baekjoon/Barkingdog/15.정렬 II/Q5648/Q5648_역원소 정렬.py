# Barkingdog/15. 정렬 II/BOJ_5648/5648_역원소 정렬.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def input_reverse_data(number_list, input_list):
    for data in input_list:
        number_list.append(int(data[::-1]))

    return number_list

if __name__ == "__main__":
    first_input = input().split()
    n = int(first_input[0])
    nums = []
    input_reverse_data(nums, first_input[1:])
    while len(nums) != n:
        after_first = input().split()
        input_reverse_data(nums, after_first)
        
    for num in sorted(nums):
        print(num)