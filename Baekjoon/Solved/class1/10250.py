import sys
import math
input = lambda: sys.stdin.readline().rstrip()

test_data_num = int(input())

for i in range(test_data_num):
    H, W, N = map(int, input().split())
    if N % H == 0:
        room_height = H
    else:
        room_height = N % H
    room_number = math.ceil(N/H)
    print(room_height * 100 + room_number)