import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    while True:
        line = input()
        if not line:  # 빈 입력 처리
            break
            
        n, s = map(int, line.split())
        if s == 0:
            break
        else:
            print(s // (n + 1))