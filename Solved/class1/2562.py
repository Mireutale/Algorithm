import sys
input = lambda: sys.stdin.readline().rstrip()

#가장 큰 숫자의 값
max_num = int(input())
#가장 큰 숫자의 번호
max_num_location = 1

for i in range(8):
    new_num = int(input())
    if max_num < new_num:
        max_num = new_num
        max_num_location = i + 2

print(max_num)
print(max_num_location)