n = int(input())
numbers = input().split()
max_n = -1000000
min_n = 1000000
for i in range(n):
    if int(numbers[i]) > max_n:
        max_n = int(numbers[i])
    if int(numbers[i]) < min_n:
        min_n = int(numbers[i])
print(min_n, max_n)