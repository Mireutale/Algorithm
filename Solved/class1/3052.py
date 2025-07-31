import sys
input = lambda: sys.stdin.readline().rstrip()

remains = [0] * 42
for i in range(10):
    num = int(input())
    remains[num % 42] += 1
    
diff_remain = 0
for i in range(len(remains)):
    if remains[i] != 0:
        diff_remain += 1

print(diff_remain)