import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        for _ in range(N):
            Ai, Bi = map(int, input().split())
            print(Ai + Bi, Ai * Bi)