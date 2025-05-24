import sys
input = lambda: sys.stdin.readline().strip()

data = input().split()
last = int(data[0])
for i in range(1, 8):
    if last + 1 == int(data[i]):
        last = int(data[i])
        if i == 7:
            print("ascending")
            break
    elif last - 1 == int(data[i]):
        last = int(data[i])
        if i == 7:
            print("descending")
            break
    else:
        print("mixed")
        break