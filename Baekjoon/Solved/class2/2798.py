#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    각 카드에는 양의 정수
    딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
    이후 딜러는 숫자 M을 크게 외친다.
    
    플레이어는 N장의 카드 중에서 3장의 카드를 골라 
    M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
    이후 선택한 카드 3장을 출력한다.
    """

    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    max_data = 0
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                if i != j and j != k:
                    now = cards[i] + cards[j] + cards[k]
                    if  now > max_data and now <= m:
                        max_data = now
    print(max_data)

    