#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    육각형 모양의 벌집 지나는 방의 개수
    1 -> 1개의 방(1개)
    2~7 -> 2개의 방(6개)
    8~19 -> 3개의 방(12개)
    20~37 -> 4개의 방(18개)
    38~61 -> 5개의 방(24개)
    """
    #1 ≤ n ≤ 1,000,000,000
    n = int(input())
    #지나간 방의 개수
    room_count = 0
    #제외한 방 개수
    room = 1
    while(n > 0):
        #1층씩 방을 지나갈때마다 더이상 지나가지 않을 방을 제외
        n -= room
        #지나간 방의 계층을 증가
        room_count += 1
        #첫번째 계층을 지나간 경우 다음단계 방 개수 6
        if room == 1:
            room = 6
        #두번째 계층 이후에는 방의 개수가 6개씩 증가
        else:
            room += 6
    print(room_count)