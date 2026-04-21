import sys
input = lambda: sys.stdin.readline().rstrip()

people = int(input())
t_size = input().split()
t_size = [int(i) for i in t_size]
t, p = map(int, input().split())
all_t = 0
for i in t_size:
    if i%t == 0:
        all_t += i//t
    else:
        all_t += (i//t + 1)
print(all_t)
print(people//p, people%p)