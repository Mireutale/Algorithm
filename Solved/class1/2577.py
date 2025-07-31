import sys
input = lambda: sys.stdin.readline().rstrip()

a = int(input())
b = int(input())
c = int(input())

finds_numbers = str(a*b*c)
numbers = [0] * 10
for i in range(len(finds_numbers)):
    numbers[int(finds_numbers[i])] += 1

for j in range(len(numbers)):
    print(numbers[j])