import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    while True:
        x, y = map(float, input().split())
        if x == 0 and y == 0:
            print("AXIS")
            break

        if x == 0 or y == 0:
            print("AXIS")
        else:
            # 1사분면
            if x > 0 and y > 0:
                print("Q1")
            # 4사분면
            elif x > 0 and y < 0:
                print("Q4")
            # 3사분면
            elif x < 0 and y < 0:
                print("Q3")
            # 2사분면
            elif x < 0 and y > 0:
                print("Q2")