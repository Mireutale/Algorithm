import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print("Hello World, Judge " + str(i+1) + "!")