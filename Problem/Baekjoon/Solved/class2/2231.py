import sys
input = lambda: sys.stdin.readline().rstrip()

# 1 <= n <= 1,000,000
n = int(input())
#생성자를 찾고싶은 값
find = n
for i in range(1, find+1):
    num = i
    part = []
    part.append(i)
    while(num > 0):
        part.append(num%10)
        num = num // 10
    #가장 작은 생성자를 찾으면 출력 후 정지
    if sum(part) == find:
        print(i)
        break
    #못 찾은 경우 -> 0을 출력 
    if i == find:
        print(0)