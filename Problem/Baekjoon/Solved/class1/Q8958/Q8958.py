import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    result = input()
    pt = 0
    all_pt = 0
    in_a_row = False
    for i in range(len(result)):
        if result[i] == "O":
            in_a_row = True
            pt += 1
            all_pt += pt    
        else:
            in_a_row = False
            pt = 0
    print(all_pt)