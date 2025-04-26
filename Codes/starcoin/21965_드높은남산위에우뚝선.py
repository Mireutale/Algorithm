#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

어떤 수열 A가 산이라는 것 -> 특정 지점 이전까지는 증가하다가, 지점 이후부터는 감소하는 것

수열이 산인지 판별
"""

if __name__ == "__main__":
    number = int(input())
    sequence = list(map(int, input().split()))
    after_top = False
    for i in range(len(sequence)-1):
        # 올라가는 형태
        if sequence[i] < sequence[i+1]:
            # 꼭대기를 지나지 않았으면 ok
            if not after_top:
                pass
            # 꼭대기를 지났는데 올라가면 no
            else:
                print("NO")
                exit()
        # 내려가는 형태
        elif sequence[i] > sequence[i+1]:
            # 처음 나온 경우, 이제 꼭대기를 지남
            if not after_top:
                after_top = True
            # 꼭대기를 
            else:
                pass
        # 평지
        else:
            print("NO")
            exit()
    print("YES")