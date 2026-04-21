import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        number = input()
        print(len(number))