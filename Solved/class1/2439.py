import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i+1):
        print("*", end="")
    print("")



"""
코드 길이가 짧은 사람
print문 하나에 다 묶어서 출력

N=int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)

"""